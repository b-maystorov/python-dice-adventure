from stats import Stats
from races import Human, Elf, Dwarf, Orc


def make_test_stats():
    return Stats(
        strength=5,
        dexterity=5,
        intelligence=5,
        vitality=5,
        luck=5,
    )


def test_human_bonus():
    stats = make_test_stats()
    Human().apply_bonus(stats)

    assert stats.strength == 6
    assert stats.intelligence == 6


def test_elf_bonus():
    stats = make_test_stats()
    Elf().apply_bonus(stats)

    assert stats.strength == 4
    assert stats.dexterity == 7
    assert stats.intelligence == 7


def test_dwarf_bonus():
    stats = make_test_stats()
    Dwarf().apply_bonus(stats)

    assert stats.strength == 7
    assert stats.dexterity == 4
    assert stats.vitality == 7


def test_orc_bonus():
    stats = make_test_stats()
    Orc().apply_bonus(stats)

    assert stats.strength == 8
    assert stats.intelligence == 3
