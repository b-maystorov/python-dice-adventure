from classes import Warrior, Mage, Rogue, Hunter, Paladin, Necromancer


def test_warrior_stats():
    stats = Warrior().get_base_stats()

    assert stats.strength == 8
    assert stats.vitality == 8


def test_mage_stats():
    stats = Mage().get_base_stats()

    assert stats.intelligence == 9


def test_rogue_stats():
    stats = Rogue().get_base_stats()

    assert stats.dexterity == 9


def test_hunter_stats():
    stats = Hunter().get_base_stats()

    assert stats.dexterity == 8


def test_paladin_stats():
    stats = Paladin().get_base_stats()

    assert stats.strength == 7
    assert stats.vitality == 7


def test_necromancer_stats():
    stats = Necromancer().get_base_stats()

    assert stats.intelligence == 9
