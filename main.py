from player import Player
from enemy import Enemy
from dice import roll_dice

hero = Player("Bilgin", 100, 10)
enemy = Enemy("Adrian", 50, 5)

print("Player:")
print(hero.name)
print(hero.health)
print(hero.is_alive())

print()

print("Enemy:")
print(enemy.name)
print(enemy.health)
print(enemy.is_alive())

print()

print("Dice roll:")
print(roll_dice())

print()

print("Player takes 10 damage")
hero.take_damage(10)
print(hero.health)

print()

print("Enemy takes 15 damage")
enemy.take_damage(15)
print(enemy.health)

print()

hero.take_damage(999)
print(hero.health)
