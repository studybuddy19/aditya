import random

def roll_dice(sides=20):
    return random.randint(1, sides)

def combat(player, enemy, enemy_hp):
    print(f"\nA wild {enemy} appears!")
    print(f"{enemy} has {enemy_hp} HP.")
    
    # Player rolls for attack
    player_roll = roll_dice(20) + player.stats["Strength"]  # Assuming Strength affects attack
    player_attack = random.randint(5, 20) + player_roll  # Base damage + roll
    print(f"{player.name} rolls a {player_roll} for attack and deals {player_attack} damage!")
    enemy_hp -= player_attack

    if enemy_hp <= 0:
        print(f"The {enemy} has been defeated!")
        return

    # Enemy rolls for attack
    enemy_roll = roll_dice(20)
    enemy_attack = random.randint(5, 15) + enemy_roll  # Base damage + roll
    print(f"The {enemy} rolls a {enemy_roll} for attack and deals {enemy_attack} damage!")
    player.hp -= enemy_attack

    if player.hp <= 0:
        print(f"{player.name} has been defeated!")
    else:
        print(f"{player.name}'s remaining HP: {player.hp}")
        print(f"{enemy}'s remaining HP: {enemy_hp}")
