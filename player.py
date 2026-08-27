from dice import roll_dice


class Player:
    def __init__(
        self,
        name: str,
        health: int,
        armor_class: int,
        attack_bonus: int,
        damage_die: int,
    ):
        self.name = name
        self.health = health
        self.armor_class = armor_class
        self.attack_bonus = attack_bonus
        self.damage_die = damage_die

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = self.health - damage

        if self.health < 0:
            self.health = 0

    def attack(self, target):
        attack_roll = roll_dice(20)
        attack_roll += self.attack_bonus

        if attack_roll >= target.armor_class:
            return True

        else:

            return False

    def roll_damage(self):
        damage = roll_dice(self.damage_die)
        return damage
