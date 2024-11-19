from unittest import TestCase, skipIf
from runner import Runner
class RunnerTest(TestCase):
    is_frozen = False
    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("Vasya")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner("Vasya")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skipIf(is_frozen,  'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Vasya")
        runner2 = Runner("Not a Vasya")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)