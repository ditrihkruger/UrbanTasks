from unittest import TestCase
from runner_and_tournament import Runner, Tournament


class TournamentTest(TestCase):
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

    def test1(self):
        tournament = Tournament(90, self.runners[0], self.runners[2])
        self.all_results = tournament.start()
        self.assertTrue(str(self.all_results[2]) == 'Ник')
    def test2(self):
        tournament = Tournament(90, *self.runners[1:])
        self.all_results = tournament.start()
        self.assertTrue(str(self.all_results[2]) == 'Ник')
    def test3(self):
        tournament = Tournament(90, *self.runners)
        self.all_results = tournament.start()
        self.assertTrue(str(self.all_results[3]) == 'Ник')
