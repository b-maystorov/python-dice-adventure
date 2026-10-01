from stats import Stats


class Human:
    name = "Human"

    def apply_bonus(self, stats: Stats) -> None:
        stats.strength += 1
        stats.intelligence += 1


class Elf:
    name = "Elf"

    def apply_bonus(self, stats: Stats) -> None:
        stats.dexterity += 2
        stats.intelligence += 2
        stats.strength -= 1


class Dwarf:
    name = "Dwarf"

    def apply_bonus(self, stats: Stats) -> None:
        stats.vitality += 2
        stats.strength += 2
        stats.dexterity -= 1


class Orc:
    name = "Orc"

    def apply_bonus(self, stats: Stats) -> None:
        stats.strength += 3
        stats.intelligence -= 2
