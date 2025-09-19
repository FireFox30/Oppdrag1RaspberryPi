import random

health = 5
food = 3
ammo = 2
nights = 10
defense = 0

print("Welcome to Zombie Survival!")

for night in range(1, nights + 1):
    print(f"\n--- Night {night} ---")
    night_event = random.choice(["zombie", "collapse", "nothing"])
    if night_event == "zombie":
        damage = max(1, 2 - defense)
        zombie_attack = 1
        if ammo > 0:
            ammo -= 1
            print("\033[1;92mA zombie attacked! Defense reduced damage to 1.\033[0m")
        else:
            absorbed = min(defense, zombie_attack)
            defense -= absorbed
            zombie_attack -= absorbed
            print(f"\033[1;92mA zombie attacked! Defense absorbed {absorbed} damage. Defense left: {defense}.\033[0m")
            if zombie_attack > 0:
                health -= zombie_attack
                print(f"\033[1;92mHealth lost: {zombie_attack}. Health left: {health}.\033[0m")
    elif night_event == "collapse":
        collapse_damage = 1
        absorbed = min(defense, collapse_damage)
        defense -= absorbed
        collapse_damage -= absorbed
        print(f"\033[1;92mPart of the cabin collapsed! Defense absorbed {absorbed} damage. Defense left: {defense}.\033[0m")
        if collapse_damage > 0:
            health -= collapse_damage
            print(f"\033[1;92mHealth lost: {collapse_damage}. Health left: {health}.\033[0m")
    
    print(f"\033[1;91mHealth: {health} | Food: {food} | Ammo: {ammo} | Defense: {defense}\033[0m")

    print("What do you want to do?")
    print("1. Search for supplies")
    print("2. Barricade the cabin")
    print("3. Rest")
    choice = input("> ")

    if choice == "1": 
        event = random.choice(["food", "ammo", "zombie", "nothing"])
        if event == "food":
            food += 1
            print("\033[1;92mYou found some food! (+1 food)\033[0m")
        elif event == "ammo":
            ammo += 1
            print("\033[1;92mYou found some ammo! (+1 ammo)\033[0m")
        elif event == "zombie":
            damage = max(0, 2 - defense)
            if ammo > 0:
                ammo -= 1
                print("\033[1;92mA zombie attacked! You used 1 ammo to kill it.\033[0m")
            else:
                health -= damage
                print(f"\033[1;92mA zombie attacked while searching! Defense reduced damage to {damage}.\033[0m")
        else:
            print("\033[1;92mYou found nothing.\033[0m")

    elif choice == "2":  # Barricade
        food -= 2
        defense += 1
        print("\033[1;92mYou reinforced the cabin! +1 defense, -2 food.\033[0m")

    elif choice == "3":  # Rest
        health += 1
        food -= 1
        print("\033[1;92mYou rested. +1 health, -1 food.\033[0m")

    else:
        print("\033[1;91mYou wasted time doing nothing.\033[0m")

    if food <= 0:
        print("\033[1;91mYou ran out of food and starved to death.\033[0m")
        break
    if health <= 0:
        print("\033[1;91mYou died from your injuries.\033[0m")
        break

else:
    print("\033[1;92mYou survived all the nights! You win!\033[0m")