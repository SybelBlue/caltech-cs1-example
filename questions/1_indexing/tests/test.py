# AUTO-GENERATED FILE
# go to https://prairielearn.readthedocs.io/en/latest/python-grader/#teststestpy for more info

from code_feedback import Feedback
from pl_helpers import name, points

from pl_stdout_test import PLStdoutTestCase

class Test(PLStdoutTestCase):
    @points(1)
    @name("finds all the treasure")
    def test_1(self):
        st_lines, ref_lines = self.st.stdout.splitlines(), self.ref.stdout.splitlines()
        score = 0
        if len(st_lines) != len(ref_lines):
            Feedback.add_feedback(f"only print {len(ref_lines)} lines!")
        else:
            mistakes = [str(i + 1) + ': you picked ' + stl for i, (stl, rfl) in enumerate(zip(st_lines, ref_lines)) if stl != rfl]
            score = max(0, len(ref_lines) - len(mistakes)) / len(ref_lines)
            Feedback.add_feedback('\n\t'.join(["you're missing the treasure on part(s):", *mistakes]))
        Feedback.set_score(score)
