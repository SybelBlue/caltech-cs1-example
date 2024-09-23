# AUTO-GENERATED FILE
# go to https://prairielearn.readthedocs.io/en/latest/python-grader/#teststestpy for more info

from code_feedback import Feedback
from pl_helpers import name, points

from pl_stdout_test import PLStdoutTestCase

class Test(PLStdoutTestCase):
    @points(0.7)
    @name('it prints!')
    def test_0(self):
        Feedback.set_score(int(bool(self.st.stdout)))

    @points(0.3)
    @name("age is just a number")
    def test_1(self):
        Feedback.set_score(int(isinstance(self.st.age, int)))
