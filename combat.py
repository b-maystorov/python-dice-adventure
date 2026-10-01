def player_attack(player, enemy):
    if player.attack(enemy):
        damage = player.roll_damage()
        enemy.take_damage(damage)

        print(f"\n{player.name} hit {enemy.name}!")
        print(f"Damage dealt: {damage}")
        print(f"{enemy.name} HP: {enemy.health}")
    else:
        print(f"\n{player.name} missed!")


def enemy_attack(enemy, player):
    if enemy.attack(player):
        damage = enemy.roll_damage()
        player.take_damage(damage)

        print(f"\n{enemy.name} hit {player.name}!")
        print(f"Damage dealt: {damage}")
        print(f"{player.name} HP: {player.health}/{player.max_health}")
    else:
        print(f"\n{enemy.name} missed!")


def run_combat(player, enemy):
    round_number = 1

    print(f"\nA wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        print(f"\n--- Round {round_number} ---")

        print("1. Attack")
        print("2. View Stats")
        print("3. Run")

        choice = input("Choose an action: ")

        if choice == "1":
            player_attack(player, enemy)

            if not enemy.is_alive():
                break

            enemy_attack(enemy, player)

            round_number += 1

        elif choice == "2":
            print()
            print(player.get_summary())

        elif choice == "3":
            print(f"\n{player.name} escaped from the fight!")
            return "escaped"

        else:
            print("Invalid choice.")

    if player.is_alive():
        print(f"\n{enemy.name} was defeated!")
        print(f"Winner: {player.name}!")
        return "win"

    print(f"\n{player.name} was defeated!")
    print(f"Winner: {enemy.name}!")
    return "lose"
