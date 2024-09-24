# AUTO-GENERATED FILE
# go to https://prairielearn.readthedocs.io/en/latest/python-grader/#teststestpy for more info

from code_feedback import Feedback
from pl_helpers import name, points

from pl_stdout_test import PLStdoutTestCase

class Test(PLStdoutTestCase):
    @points(1)
    @name('it prints!')
    def test_0(self):
        Feedback.set_score(int(bool(self.st.stdout)))

    @points(3)
    @name("got it right!")
    def test_1(self):
        # only runs if there's no syntax error after running student code
        points = 0

        ref_output = list(set(filter(bool, self.st.stdout.splitlines())))
        ref_output.sort()
        std_output = list(set(filter(bool, self.ref.stdout.splitlines())))
        std_output.sort()

        # only checks list len and top-level type (which we knew already)
        if Feedback.check_list('output', ref_output, std_output):
            points = 3 * int(ref_output == std_output)

        Feedback.set_score(points)
