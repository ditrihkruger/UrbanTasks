from unittest import TestCase, skipIf
from rt_with_exceptions import Runner
import logging
import tests_12_4

class RunnerTest(TestCase):
    is_frozen = False
    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = Runner("Vasya",-5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning("Неверная скорость для Runner")

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner("Vasya", "H")
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(f'"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning("Неверный тип данных для объекта Runner")


    @skipIf(is_frozen,  'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("Vasya")
        runner2 = Runner("Not a Vasya")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)