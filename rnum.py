import time, random

print("Guess the number!\n")
time.sleep(2)
print("Guess the number between 0 - 20")
time.sleep(1.5)
print("You have 3 tryes!")
print("Good luck\n")

number = random.randint(0, 20)
tryes = 0

while True:
    tryes += 1

    if tryes == 4:
        print("\nYou run out of Tryes!")
        print(f"ANSWEAR = {number}")
        break

    print(f"\nTryes = {tryes}")
    ans = input("?: ")

    if int(ans) < 0:
        print(f"\nValue... {ans} is too low, Please choose another number!")
        ans = input("?: ")
    
    if int(ans) > 20:
        print(f"\nValue... {ans} is too big, Please choose another number!")
        ans = input("?: ")

    if int(number) < int(ans):
        print("\nYou weren't lucky ... The number is smaller!")
    
    if int(number) > int(ans):
        print("\nYou weren't lucky ... The number is bigger!")

    if int(number) == int(ans):
        print("\nGood JOB, You WON nothing!")
        break

time.sleep(1)
print("\nPress ENTER to quit!")
input()