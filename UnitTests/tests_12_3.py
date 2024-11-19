from unittest import TestSuite, TextTestRunner
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest

variable2 = TestSuite()
variable2.addTest(RunnerTest)
variable2.addTest(TournamentTest)
variable2.addTest(TextTestRunner(verbosity = 2))