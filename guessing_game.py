"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

from random import randint


def welcome():
    print("""

    -------> Welcome to the Number Guessing Game <-------
    In this fun console game you the player will be tasked with
    guessing what number I am thinking.

    Try to guess in as little trys as possible and beat the high score!
    """)


welcome()


def start_game():

    # Difficultly setting
    diff_setting = input("Choose a difficultly setting: [E]asy, [M]edium, [H]ard, [C]razy\n> ").upper()
    if diff_setting == 'E':
        difficultly = 10
    elif diff_setting == 'M':
        difficultly = 50
    elif diff_setting == 'H':
        difficultly = 100
    elif diff_setting == 'C':
        difficultly = 1000
    else:
        difficultly = 50

    # Stored correct answer
    answer = randint(0, difficultly)

    # Game Mechanic
    while True:
        try:
            player_guess = int(input("What number am I thinking of?\n> "))

            if player_guess > difficultly or player_guess < 0:
                print(f"Out of Range: Guess should be between 0 and {difficultly}. Try again.\n")
                continue
            elif answer < player_guess:
                print("Guess it too high!")
                continue
            elif answer > player_guess:
                print("Guess is too low!")
                continue
            elif answer == player_guess:
                print("Wow you've guessed right! Good Job!\n")
                play_again = input("\nWould you like to play again? [Y]es/[N]o\n> ").upper()

                if play_again == 'Y':
                    start_game()
                elif play_again == 'N':
                    print("Thank you for playing the Guessing Game! Good-Bye.")
                    break
                else:
                    print("Invalid choice: Try again\n")
                    continue
        except ValueError:
            print("INVALID: Guess must be a number try again.\n")
            continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
