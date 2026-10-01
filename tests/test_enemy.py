from enemy import Enemy


def test_enemy_creation():
    enemy = Enemy(
        name="Goblin",
        health=20,
        armor_class=12,
        attack_bonus=2,
        damage_die=6,
    )

    assert enemy.name == "Goblin"
    assert enemy.health == 20
    assert enemy.armor_class == 12


def test_enemy_take_damage():
    enemy = Enemy(
        name="Goblin",
        health=20,
        armor_class=12,
        attack_bonus=2,
        damage_die=6,
    )

    enemy.take_damage(7)

    assert enemy.health == 13


def test_enemy_health_cannot_be_negative():
    enemy = Enemy(
        name="Goblin",
        health=20,
        armor_class=12,
        attack_bonus=2,
        damage_die=6,
    )

    enemy.take_damage(100)

    assert enemy.health == 0
    assert enemy.is_alive() is False
