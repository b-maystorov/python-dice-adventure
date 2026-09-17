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
