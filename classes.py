from stats import Stats


class Warrior:
    name = "Warrior"

    def get_base_stats(self):
        return Stats(
            strength=8,
            dexterity=4,
            intelligence=2,
            vitality=8,
            luck=3,
        )


class Mage:
    name = "Mage"

    def get_base_stats(self):
        return Stats(
            strength=2,
            dexterity=4,
            intelligence=9,
            vitality=4,
            luck=4,
        )


class Rogue:
    name = "Rogue"

    def get_base_stats(self):
        return Stats(
            strength=4,
            dexterity=9,
            intelligence=3,
            vitality=4,
            luck=7,
        )


class Hunter:
    name = "Hunter"

    def get_base_stats(self):
        return Stats(
            strength=5,
            dexterity=8,
            intelligence=3,
            vitality=5,
            luck=6,
        )


class Paladin:
    name = "Paladin"

    def get_base_stats(self):
        return Stats(
            strength=7,
            dexterity=3,
            intelligence=5,
            vitality=7,
            luck=4,
        )


class Necromancer:
    name = "Necromancer"

    def get_base_stats(self):
        return Stats(
            strength=2,
            dexterity=3,
            intelligence=9,
            vitality=5,
            luck=5,
        )
