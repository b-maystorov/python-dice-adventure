import unittest

from enemy import Enemy


class TestEnemy(unittest.TestCase):
    def test_take_damage_reduces_health(self):
        enemy = Enemy("Test Enemy", 20, 12, 2, 6)

        enemy.take_damage(5)

        self.assertEqual(enemy.health, 15)

    def test_health_cannot_go_below_zero(self):
        enemy = Enemy("Test Enemy", 20, 12, 2, 6)

        enemy.take_damage(100)

        self.assertEqual(enemy.health, 0)

    def test_enemy_is_alive(self):
        enemy = Enemy("Test Enemy", 20, 12, 2, 6)

        self.assertTrue(enemy.is_alive())

    def test_enemy_is_not_alive_at_zero_health(self):
        enemy = Enemy("Test Enemy", 0, 12, 2, 6)

        self.assertFalse(enemy.is_alive())


if __name__ == "__main__":
    unittest.main()
