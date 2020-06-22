import json, string, random, time

print("1. Add password\n2. Get password")

def rChar(x):
    return "".join(random.choice(string.ascii_letters + string.digits) for x in range(x))

while True:
    with open("passwords.json", "r") as f:
        passwords = json.load(f)

    choice = input("?: ")
    
    site = input("\nSite name: ")
    site = site.lower()

    if choice == '1':

        if site in passwords:

            print(f"\nThe site already exist!")
            msg = input("Do you want to change it? Y/N\n")
            passwords.pop(str(site))
            x = 0
        
        else:
            msg = "nope"
            x = 1
            

        if msg.lower() == "y" or x == 1:

            print(f"\npass: {rChar(18)}")

            passwords[str(site)] = str(rChar(18))

            with open("passwords.json", "w") as f:
                json.dump(passwords, f, indent=4)
            
            time.sleep(2.4)

    elif choice == '2':
        
        if site in passwords:

            print("\n password: " + passwords[site])
        
        else:
            print("\nThis site doesn't exist in database!")
        
        time.sleep(2.4)


    else:
        print("Error: Invalide characters")

    print("\n1. Add password\n2. Get password")
