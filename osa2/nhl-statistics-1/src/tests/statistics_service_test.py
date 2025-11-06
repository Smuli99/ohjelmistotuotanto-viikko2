import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan oliolle
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    # Metodin search testaus
    def test_find_specific_player(self):
        player = self.stats.search("Lemieux")

        self.assertEqual(player.name, "Lemieux")

    def test_return_none_if_player_name_is_invalid(self):
        player = self.stats.search("Litmanen")

        self.assertEqual(player, None)

    # Metodin team testaus
    def test_find_all_players_from_specific_team(self):
        players = self.stats.team("EDM")

        # löytää 3 pelaajaa
        self.assertEqual(len(players), 3)

        # oikeat pelaajat löytyvät
        names = [player.name for player in players]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_return_empty_array_if_invalid_team(self):
        players = self.stats.team("MAN")

        # tyhjä lista
        self.assertEqual(len(players), 0)

    # Metodin top testaus
    def test_return_specific_amount_of_top_point_players(self):
        players = self.stats.top(1)

        # palauttaa yhden pelaajan jolla on eniten pisteitä
        self.assertEqual(len(players), 1)

        names = [player.name for player in players]
        self.assertEqual(names, ["Gretzky"])

    def test_return_three_top_point_players_in_order(self):
        players = self.stats.top(3)

        # palautaa kolme pelaajaa
        self.assertEqual(len(players), 3)

        # palauttaa kolme parasta pistemiestä järjestyksessä
        names = [player.name for player in players]
        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_return_empty_array_if_0_or_less_as_paramiter(self):
        players = self.stats.top(0)

        self.assertEqual(len(players), 0)
