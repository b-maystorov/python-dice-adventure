from stats import Stats


class Orc:
    name = "Orc"

    def apply_bonus(self, stats):
        stats.strength = stats.strength + 3
        stats.intelligence = stats.intelligence - 2


class Elf:
    name = "Elf"

    def apply_bonus(self, stats):
        stats.dextery
