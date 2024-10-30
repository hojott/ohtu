import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_pelaaja_olemassa(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_pelaaja_ei_olemassa(self):
        player = self.stats.search("Kaapo")
        self.assertEqual(player, None)

    def test_team_tiimi_olemassa(self):
        team = self.stats.team("EDM")
        self.assertEqual(set(p.name for p in team), {"Semenko", "Kurri", "Gretzky"})

    def test_team_tiimi_ei_olemassa(self):
        team = self.stats.team("ABC")
        self.assertEqual(team, [])

    def test_top_yksi(self):
        top = self.stats.top(0)
        self.assertEqual(top[-1].name, "Gretzky")
    
    def test_top_viisi(self):
        top = self.stats.top(4)
        self.assertEqual([p.name for p in top], ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"])

    def test_top_liikaa(self):
        func = lambda: self.stats.top(8)
        self.assertRaises(IndexError, func)

    def test_top_negatiivinen(self):
        top = self.stats.top(-1)
        self.assertEqual(top, [])