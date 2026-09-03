import unittest

from dice import roll_dice


class TestDice(unittest.TestCase):
    def test_d20_result_stays_between_1_and_20(self):
        for _ in range(100):
            result = roll_dice(20)

            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
