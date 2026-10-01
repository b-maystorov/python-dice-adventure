from player import Player
from races import Human, Elf
from classes import Warrior, Mage


def test_human_warrior_creation():
    player = Player(
        name="Test Hero",
        race=Human(),
        char_class=Warrior(),
    )

    assert player.stats.strength == 9
    assert player.stats.dexterity == 4
    assert player.stats.intelligence == 3
    assert player.stats.vitality == 8

    assert player.max_health == 60
    assert player.health == 60
    assert player.armor_class == 14
    assert player.attack_bonus == 4
    assert player.damage_die == 8


def test_elf_mage_creation():
    player = Player(
        name="Test Mage",
        race=Elf(),
        char_class=Mage(),
    )

    assert player.stats.strength == 1
    assert player.stats.dexterity == 6
    assert player.stats.intelligence == 11

    assert player.primary_stat_value == 11
    assert player.attack_bonus == 5
    assert player.damage_die == 8


def test_player_take_damage():
    player = Player(
        name="Test Hero",
        race=Human(),
        char_class=Warrior(),
    )

    player.take_damage(10)

    assert player.health == 50


def test_health_cannot_be_negative():
    player = Player(
        name="Test Hero",
        race=Human(),
        char_class=Warrior(),
    )

    player.take_damage(500)

    assert player.health == 0
    assert player.is_alive() is False
