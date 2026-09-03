import unittest

from player import Player


class TestPlayer(unittest.TestCase):
    def test_take_damage_reduces_health(self):
        player = Player("Test Hero", 30, 14, 3, 8)

        player.take_damage(5)

        self.assertEqual(player.health, 25)

    def test_health_cannot_go_below_zero(self):
        player = Player("Test Hero", 30, 14, 3, 8)

        player.take_damage(100)

        self.assertEqual(player.health, 0)

    def test_player_is_alive(self):
        player = Player("Test Hero", 30, 14, 3, 8)

        self.assertTrue(player.is_alive())

    def test_player_is_not_alive_at_zero_health(self):
        player = Player("Test Hero", 0, 14, 3, 8)

        self.assertFalse(player.is_alive())


if __name__ == "__main__":
    unittest.main()
