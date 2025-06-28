import random

def main():
    play = "y"
    while play == "y":
        print("SELECT YOUR WEAPON (1-3)")
        print("-------------------------")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_input = input("Enter your Weapon: ")
        user_weapon = int(user_input)

        opponent_weapon = random.randint(1, 3)

        if user_weapon == opponent_weapon:
            print("It's a tie!")
        elif user_weapon == 1 and opponent_weapon == 3:
            print("You win, rock crushes scissors!")
        elif user_weapon == 2 and opponent_weapon == 1:
            print("You win, paper covers rock!")
        elif user_weapon == 3 and opponent_weapon == 2:
            print("You win, scissors cuts paper!")
        elif opponent_weapon == 1 and user_weapon == 3:
            print("You lose, rock crushes scissors!")
        elif opponent_weapon == 2 and user_weapon == 1:
            print("You lose, paper covers rock!")
        elif opponent_weapon == 3 and user_weapon == 2:
            print("You lose, scissors cuts paper!")

        play = input("Want to play again (y/n): ")

    print("Completed by, Your Name Here")

main()
