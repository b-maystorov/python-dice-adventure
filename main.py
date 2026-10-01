from character_creation import create_player
from combat import run_combat
from enemy import Enemy


def main():
    print("================================")
    print("      PYTHON DICE ADVENTURE")
    print("================================")

    hero = create_player()

    enemy = Enemy(
        name="Adrian",
        health=20,
        armor_class=12,
        attack_bonus=2,
        damage_die=6,
    )

    run_combat(hero, enemy)


if __name__ == "__main__":
    main()
