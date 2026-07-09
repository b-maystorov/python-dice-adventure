from player import Player
from enemy import Enemy
from dice import roll_dice

hero = Player("Bilgin", 0, 10)
print(hero.name)
print(hero.health)
print(hero.is_alive())

enemy = Enemy("Adrian", 50, 10)
print(enemy.name)
print(enemy.health)
print(enemy.is_alive())

print(roll_dice())
print(roll_dice())
print(roll_dice())
