from unittest import TestCase, skipIf
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.runners = [
           Runner('Усэйн', 10),
           Runner('Андрей', 9),
           Runner('Ник', 3)
        ]

    @classmethod
    def tearDownClass(self):
        for result in self.all_results:
            print(result)

    @skipIf(is_frozen, 'Тест Заморожен')
    def test1(self):
        tournament = Tournament(90, self.runners[0], self.runners[2])
        self.all_results = tournament.start()
        self.assertTrue(str(self.all_results[2]) == 'Ник')

    @skipIf(is_frozen, 'Тест Заморожен')
    def test2(self):
        tournament = Tournament(90, *self.runners[1:])
        self.all_results = tournament.start()
        self.assertTrue(str(self.all_results[2]) == 'Ник')

    @skipIf(is_frozen, 'Тест Заморожен')
    def test3(self):
        tournament = Tournament(90, *self.runners)
        self.all_results = tournament.start()
        self.assertTrue(str(self.all_results[3]) == 'Ник')
