from dice import roll_dice


def test_roll_dice_range():
    for _ in range(100):
        result = roll_dice(6)

        assert 1 <= result <= 6
