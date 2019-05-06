"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

from random import randint


def welcome():
    print("""

    -------> Welcome to the Number Guessing Game <-------
    In this fun console game you the player will be tasked with
    guessing what number I am thinking.

    Try to guess in as little trys as possible and win a prize!
    """)






def start_game():
    welcome()
    diff_setting = input("Choose a difficultly setting\n[E]asy, [M]edium, [H]ard, [C]razy:> ").Upper()
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

    answer = randint(0, difficultly)


    '''Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    '''
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
