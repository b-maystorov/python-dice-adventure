from dice import roll_dice


class Enemy:
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

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> None:
        self.health -= damage

        if self.health < 0:
            self.health = 0

    def attack(self, target) -> bool:
        attack_roll = roll_dice(20)
        total_attack = attack_roll + self.attack_bonus

        return total_attack >= target.armor_class

    def roll_damage(self) -> int:
        return roll_dice(self.damage_die)
