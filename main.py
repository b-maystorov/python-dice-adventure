from player import Player
from enemy import Enemy

# Ask the user for their character's name.
player_name = input("Enter your hero's name: ")

# Create both characters once so health persists between rounds.
hero = Player(player_name, 30, 14, 3, 8)
enemy = Enemy("Adrian", 20, 12, 2, 6)

round_number = 1

# Remembers whether combat ended because the player escaped.
player_ran_away = False


# Combat continues while both characters are alive.
while hero.is_alive() == True and enemy.is_alive() == True:
    print(f"\n--- Round {round_number} ---")

    print("1. Attack")
    print("2. Run")

    choice = input("Choose an action: ")

    # Choosing 2 stops combat without declaring a winner.
    if choice == "2":
        player_ran_away = True
        print(f"{hero.name} escaped from the fight!")
        break

    # PLAYER TURN
    attack_hit = hero.attack(enemy)

    if attack_hit == True:
        print(f"{hero.name} hit {enemy.name}!")

        damage = hero.roll_damage()
        enemy.take_damage(damage)

        print(f"Damage dealt: {damage}")
        print(f"{enemy.name} remaining health: {enemy.health}")

    else:
        print(f"{hero.name} missed!")

    # A defeated enemy cannot perform another attack.
    if enemy.is_alive() == False:
        break

    # ENEMY TURN
    enemy_attack_hit = enemy.attack(hero)

    if enemy_attack_hit == True:
        print(f"{enemy.name} hit {hero.name}!")

        enemy_damage = enemy.roll_damage()
        hero.take_damage(enemy_damage)

        print(f"Damage dealt: {enemy_damage}")
        print(f"{hero.name} remaining health: {hero.health}")

    else:
        print(f"{enemy.name} missed!")

    # One complete round ends after both turns.
    round_number += 1


# Determine why combat ended.
if player_ran_away == True:
    print("Combat ended because the player ran away.")

elif hero.is_alive() == True:
    print(f"Winner: {hero.name}!")

else:
    print(f"Winner: {enemy.name}!")
