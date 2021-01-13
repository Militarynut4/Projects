import random, colorama, os, time
colorama.init(convert=True)
clear = lambda : os.system("cls")

def Main():
    while True:
        while True:
            players = []
            display_teams = []
            clear()
            banner()
            print(colorama.Fore.YELLOW + "Note! Type DONE to stop adding players")
            print(colorama.Fore.YELLOW + "Note! Type RESET to reset the list")
            print(colorama.Fore.WHITE + "Add player to list!")
            player_count = 1
            while True:
                user = input(f"{player_count}: ")
                if user.lower() == "done" or user.lower() == 'reset':
                    break
                players.append(user)
                player_count += 1
            if user.lower() == "done":
                break
        while True:
            clear()
            banner()
            print(colorama.Fore.YELLOW + f"Note! You can't have less then 2 players or more then {len(players) - 1}")
            print(colorama.Fore.WHITE + "How many players do you want in one team?")
            teams = input("?:")
            try:
                teams = int(teams)
                if teams != 1 and teams < len(players):
                    break
            except:
                pass
        clear()
        banner()
        while len(players) != 0:
            if len(players) < int(teams):
                teams = len(players)
            text = ""
            for x in range(0, teams):
                user = random.choice(players)
                text = text + user + ", "
                players.remove(user)
            text = text[:-2]
            display_teams.append(text)
        for x, y in enumerate(display_teams):
            print(colorama.Fore.WHITE + f"Team {x + 1} | {y} ")
        input(colorama.Fore.RED + f"\n\nPress ENTER to continue")
        

def banner():
    print(colorama.Fore.MAGENTA + """
░█████╗░███╗░░██╗██████╗░██████╗░███████╗██╗██████╗░███████╗██╗░░░██╗
██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔════╝██║██╔══██╗╚════██║██║░░░██║
███████║██╔██╗██║██║░░██║██████╔╝█████╗░░██║██████╔╝░░███╔═╝╚██╗░██╔╝
██╔══██║██║╚████║██║░░██║██╔══██╗██╔══╝░░██║██╔══██╗██╔══╝░░░╚████╔╝░
██║░░██║██║░╚███║██████╔╝██║░░██║███████╗██║██║░░██║███████╗░░╚██╔╝░░
╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░""")
    print("\n")

if __name__ == "__main__":
    Main()
