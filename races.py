from stats import Stats


class Orc:
    name = "Orc"

    def apply_bonus(self, stats):
        stats.strength = stats.strength + 3
        stats.intelligence = stats.intelligence - 2


class Elf:
    name = "Elf"

    def apply_bonus(self, stats):
        stats.dexterity = stats.dexterity + 2
        stats.intelligence = stats.intelligence + 2
        stats.strength = stats.strength - 2


class Human:
    name = "Human"

    def apply_bonus(self, stats):
        stats.intelligence = stats.intelligence + 1
        stats.strength = stats.strength + 1


class Dwarf:
    name = "Dwarf"

    def apply_bonus(self, stats):
        stats.vitality = stats.vitality + 2
        stats.strength = stats.strength + 2
        stats.dexterity = stats.dexterity - 1
