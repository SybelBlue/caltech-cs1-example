# AUTO-GENERATED FILE
# go to https://prairielearn.readthedocs.io/en/latest/python-grader/#teststestpy for more info

from pl_helpers import name, points # type: ignore
from code_feedback import Feedback # type: ignore

from pl_stdout_test import PLStdoutTestCase

class Test(PLStdoutTestCase):
    @points(4)
    @name("gets the correct cost")
    def test_1(self):
        Feedback.set_score(self.st.cost == self.ref.cost)
