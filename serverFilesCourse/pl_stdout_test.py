# a cursed workaround to catch the stdout of the student and reference
# solutions in their proper contexts

import json
import os
import os.path as path
import random
import sys
import pl_helpers
import matplotlib

from copy import deepcopy
from types import ModuleType
from collections import namedtuple

from code_feedback import Feedback
from pl_execute import try_read, set_random_seed, UserCodeFailed
from pl_unit_test import PLTestCase

from contextlib import redirect_stdout
import io

class PLStdoutTestCase(PLTestCase):
    @classmethod
    def setUpClass(self):
        """
        On start, run the user code and generate answer tuples.
        """
        Feedback.set_test(self)
        base_dir = os.environ.get("MERGE_DIR")
        filenames_dir = os.environ.get("FILENAMES_DIR")
        self.student_code_abs_path = path.join(base_dir, self.student_code_file)

        # Load data so that we can use it in the test cases
        filenames_dir = os.environ.get("FILENAMES_DIR")
        with open(path.join(filenames_dir, "data.json"), encoding="utf-8") as f:
            self.data = json.load(f)

        ref_result, ref_stdout, student_result, student_stdout, plot_value = execute_code(
            path.join(filenames_dir, "ans.py"),
            path.join(base_dir, self.student_code_file),
            self.include_plt,
            path.join(base_dir, "output.txt"),
            self.iter_num,
            self.ipynb_key,
        )
        answerTuple = namedtuple("answerTuple", ('stdout', *ref_result.keys()))
        self.ref = answerTuple(stdout=ref_stdout, **ref_result)
        studentTuple = namedtuple("studentTuple", ('stdout', *student_result.keys()))
        self.st = studentTuple(stdout=student_stdout, **student_result)
        self.plt = plot_value
        if self.include_plt:
            self.display_plot()


# a modified copy of execute_code from prairielearn that captures stdouts:
# https://github.com/PrairieLearn/PrairieLearn/blob/203dd139276825c16b9e2a2589116ca55aca7cfc/graders/python/python_autograder/pl_execute.py#L33
def execute_code(
    fname_ref,
    fname_student,
    include_plt=False,
    console_output_fname=None,
    test_iter_num=0,
    ipynb_key="#grade",
):
    """
    execute_code(fname_ref, fname_student)

    Helper function for running user code.

    - fname_ref: Filename for the reference (answer) code.
    - fname_student: Filename for the submitted student answer code.
    - include_plt: If true, plots will be included in grading results.
    - console_output_fname: Filename to redirect console output to.
    - test_iter_num: The iteration number of this test, when test cases are run multiple times.

    Returns:
    - ref_result: A named tuple with reference variables
    - ref_result: The reference's captured stdout
    - student_result: A named tuple with submitted student variables
    - student_stdout: The student's captured stdout
    - plot_value: Any plots made by the student
    """

    filenames_dir = os.environ.get("FILENAMES_DIR")

    with open(path.join(filenames_dir, "data.json"), encoding="utf-8") as f:
        data = json.load(f)
    with open(path.join(filenames_dir, "setup_code.py"), "r", encoding="utf-8") as f:
        str_setup = f.read()
    with open(fname_ref, "r", encoding="utf-8") as f:
        str_ref = f.read()

    # Read in leading, trailing code
    str_leading = try_read(path.join(filenames_dir, "leading_code.py"))
    str_trailing = try_read(path.join(filenames_dir, "trailing_code.py"))

    # Read student code (and transform if necessary) and append leading/trailing code
    with open(fname_student, "r", encoding="utf-8") as f:
        filename, extension = path.splitext(fname_student)
        if extension == ".ipynb":
            str_student = pl_helpers.extract_ipynb_contents(f, ipynb_key)
        else:
            str_student = f.read()
    str_student = str_leading + str_student + str_trailing

    with open(path.join(filenames_dir, "test.py"), encoding="utf-8") as f:
        str_test = f.read()

    # Delete sensitive code so students can't read e.g. test cases or setup code
    os.remove(path.join(filenames_dir, "data.json"))
    os.remove(fname_ref)
    os.remove(path.join(filenames_dir, "setup_code.py"))
    try:
        os.remove(path.join(filenames_dir, "leading_code.py"))
    except FileNotFoundError:
        pass
    try:
        os.remove(path.join(filenames_dir, "trailing_code.py"))
    except FileNotFoundError:
        pass
    os.remove(path.join(filenames_dir, "test.py"))

    repeated_setup_name = "repeated_setup()"
    if repeated_setup_name not in str_setup:
        repeated_setup_name = "pass"

    # Seed student code and answer code with same seed
    seed = random.randint(0, (2**32) - 1)

    setup_code = {"test_iter_num": test_iter_num, "data": data}
    # make all the variables in setup_code.py available to ans.py
    exec(str_setup, setup_code)
    exec(repeated_setup_name, setup_code)

    names_for_user = []
    for variable in data["params"]["names_for_user"]:
        names_for_user.append(variable["name"])

    # Make copies of variables that go to the user so we do not clobber them
    ref_code = {}
    for i, j in setup_code.items():
        if (not (i == "__builtins__" or isinstance(j, ModuleType))) and (
            i in names_for_user
        ):
            ref_code[i] = j
    ref_code = deepcopy(ref_code)

    # Add any other variables to reference namespace and do not copy
    for i, j in setup_code.items():
        if not (
            i == "__builtins__" or isinstance(j, ModuleType) or i in names_for_user
        ):
            ref_code[i] = j
    set_random_seed(seed)
    ref_stdout = io.StringIO()
    with redirect_stdout(ref_stdout):
        # ref_code contains the correct answers
        exec(str_ref, ref_code)
    ref_stdout = ref_stdout.getvalue()

    if include_plt:
        for i, j in ref_code.items():
            if isinstance(j, ModuleType):
                if j.__dict__["__name__"] == "matplotlib.pyplot":
                    j.close("all")

    # make only the variables listed in names_for_user available to student
    names_from_user = []
    for variable in data["params"]["names_from_user"]:
        names_from_user.append(variable["name"])

    exec(repeated_setup_name, setup_code)

    student_code = {}
    for i, j in setup_code.items():
        if (not (i == "__builtins__" or isinstance(j, ModuleType))) and (
            i in names_for_user
        ):
            student_code[i] = j
    student_code = deepcopy(student_code)

    # Execute student code
    student_stdout = io.StringIO()
    with redirect_stdout(student_stdout):
        set_random_seed(seed)

        try:
            exec(str_student, student_code)
            err = None
        except Exception:
            err = sys.exc_info()

        # Now that user code has been run, replace deleted files in case we are to run the tests again.
        with open(path.join(filenames_dir, "data.json"), "w", encoding="utf-8") as f:
            json.dump(data, f)
        with open(fname_ref, "w", encoding="utf-8") as f:
            f.write(str_ref)
        with open(path.join(filenames_dir, "setup_code.py"), "w", encoding="utf-8") as f:
            f.write(str_setup)
        if len(str_leading) > 0:
            with open(
                path.join(filenames_dir, "leading_code.py"), "w", encoding="utf-8"
            ) as f:
                f.write(str_leading)
        if len(str_trailing) > 0:
            with open(
                path.join(filenames_dir, "trailing_code.py"), "w", encoding="utf-8"
            ) as f:
                f.write(str_trailing)
        with open(path.join(filenames_dir, "test.py"), "w", encoding="utf-8") as f:
            f.write(str_test)
        if err is not None:
            raise UserCodeFailed(err)

    student_stdout = student_stdout.getvalue()

    ref_result = {}
    for i, j in ref_code.items():
        if not (i.startswith("_") or isinstance(j, ModuleType)):
            ref_result[i] = j

    student_result = {}
    for name in names_from_user:
        student_result[name] = student_code.get(name, None)

    plot_value = None
    if include_plt:
        for key in list(student_code):
            if isinstance(student_code[key], ModuleType):
                if student_code[key].__dict__["__name__"] == "matplotlib.pyplot":
                    plot_value = student_code[key]
        if not plot_value:
            import matplotlib

            matplotlib.use("Agg")
            import matplotlib.pyplot

            plot_value = matplotlib.pyplot

    # Re-seed before running tests
    set_random_seed()
    return ref_result, ref_stdout, student_result, student_stdout, plot_value