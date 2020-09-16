import random, time, sys, os

clear = lambda: os.system('cls')
name = input("NickName: ")
time.sleep(1)
clear()

print("Beat the boss!")
time.sleep(2.5)

boss_health = 125
user_health = 100

battle = 0

while (boss_health >= 1) and (user_health >= 1):
    clear()

    boss_damage = random.randint(6, 12)
    user_damage = random.randint(1, 16)
    mortal = random.randint(8, 20)
    user_heal = random.randint(4, 16)
    boss_heal = random.randint(2, 12)
    battle += 1
    
    print(f"ROUND {battle}!")
    time.sleep(1.2)
    print("Boss health: " + str(boss_health))
    print(f"{name.strip()} health: " + str(user_health))

    time.sleep(1)

    if user_health == 100:
        print("\nYou can use only hit / heal")
        skema = input("?: ")
    else:
        skema = input("\n?: ")


    if skema == "hit":
        r = random.randint(1, 6)
        
        if r == 1:
            boss_mortal = user_damage + mortal
            boss_health -= boss_mortal
            
            print(f"\nMORTAL HIT! {name.strip()} punched for {boss_mortal} DMG!")
            
        else:
            boss_health -= user_damage

            print(f"\n{name.strip()} punched for {user_damage} DMG!")
    
    elif skema == "heal":
        user_health += user_heal
        print(f"\n{name.strip()} increased health with {user_heal} HP")

    else:
        print("\n!WRONG VALUE!")
        boss_health -= user_damage
        print(f"{name.strip()} punched for {user_damage} DMG!")

    time.sleep(1.2)

    choice = random.randint(1, 5)

    if choice <= 4:
        
        user_health -= boss_damage
        print(f"Boss punched you for {boss_damage} DMG!")
    
    else:
        if boss_health <= 55:

            boss_health += boss_heal
            print(f"Boss increased health with {boss_heal} HP")
        else:
            user_health -= boss_damage
            print(f"Boss punched you for {boss_damage} DMG!")

    print("\n3")
    time.sleep(1)
    print("\t2")
    time.sleep(1)
    print("\t\t1")
    time.sleep(1)


if user_health < boss_health:
    print(f"\nYou got owned by BOSS!")
    print(f"Boss HP = {boss_health}")
    print(f"User HP = {user_health}")

elif boss_health < user_health:
    print(f"\nYou defeated BOSS, Good job!")
    print(f"Boss HP = {boss_health}")
    print(f"User HP = {user_health}")

else:
    print(f"\nHow tf you both died?") 


time.sleep(1.5)
print(f"\nPRESS ENTER KEY TO EXIT")
input()
