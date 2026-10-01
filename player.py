from dice import roll_dice


class Player:
    def __init__(self, name: str, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class

        # Get fresh base stats from the selected class.
        self.stats = char_class.get_base_stats()

        # Apply the selected race bonuses.
        race.apply_bonus(self.stats)

        # Current HP starts at the calculated maximum.
        self.health = self.max_health

    @property
    def max_health(self) -> int:
        return 20 + self.stats.vitality * 5

    @property
    def armor_class(self) -> int:
        return 10 + self.stats.dexterity

    @property
    def primary_stat_value(self) -> int:
        stat_name = self.char_class.primary_stat
        return getattr(self.stats, stat_name)

    @property
    def attack_bonus(self) -> int:
        return self.primary_stat_value // 2

    @property
    def damage_die(self) -> int:
        primary = self.primary_stat_value

        if primary >= 8:
            return 8
        elif primary >= 5:
            return 6
        else:
            return 4

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

    def get_summary(self) -> str:
        return (
            f"{self.name} - {self.race.name} {self.char_class.name}\n"
            f"HP: {self.health}/{self.max_health}\n"
            f"AC: {self.armor_class}\n"
            f"Attack Bonus: +{self.attack_bonus}\n"
            f"Damage: d{self.damage_die}\n"
            f"STR: {self.stats.strength}\n"
            f"DEX: {self.stats.dexterity}\n"
            f"INT: {self.stats.intelligence}\n"
            f"VIT: {self.stats.vitality}\n"
            f"LUK: {self.stats.luck}"
        )
