from player import Player

from races import Human, Elf, Dwarf, Orc

from classes import (
    Warrior,
    Mage,
    Rogue,
    Hunter,
    Paladin,
    Necromancer,
)

RACES = {
    "1": Human,
    "2": Elf,
    "3": Dwarf,
    "4": Orc,
}


CLASSES = {
    "1": Warrior,
    "2": Mage,
    "3": Rogue,
    "4": Hunter,
    "5": Paladin,
    "6": Necromancer,
}


def choose_race():
    while True:
        print("\nChoose your race:")
        print("1. Human")
        print("2. Elf")
        print("3. Dwarf")
        print("4. Orc")

        choice = input("> ")

        if choice in RACES:
            return RACES[choice]()

        print("Invalid choice. Try again.")


def choose_class():
    while True:
        print("\nChoose your class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        print("4. Hunter")
        print("5. Paladin")
        print("6. Necromancer")

        choice = input("> ")

        if choice in CLASSES:
            return CLASSES[choice]()

        print("Invalid choice. Try again.")


def create_player() -> Player:
    print("\n=== CREATE YOUR HERO ===")

    name = input("Enter your hero's name: ")

    race = choose_race()
    char_class = choose_class()

    player = Player(
        name=name,
        race=race,
        char_class=char_class,
    )

    print("\n=== CHARACTER CREATED ===")
    print(player.get_summary())

    return player
