from unittest import TestCase
from runner import Runner
class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("Vasya")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Vasya")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Vasya")
        runner2 = Runner("Not a Vasya")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)