import os
import random
from words import words



def welcome():
    """
    Show welcome message and ask user if they would like to see instructions.
    """
    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Welcome message.
    print("{:-^80}".format("HANGMAN"))
    print("\n")

    print("{:^80}".format("Welcome to Hangman!\n"))
    print("{:^80}".format("Before we start, would you like to see "))
    print("{:^80}".format("the instructions or are you good to go?\n"))
    # Ask user to choose if they want to see instructions or not.
    print("{:^80}".format("Please type 1 to see the instructions,"))
    see_instructions = input("{:^80}".format("or 2 for good to go!:\n"))
    # Make sure users input is valid.
    while see_instructions != "1" and see_instructions != "2":
        print("{:^80}".format("Invalid input,"))
        print("{:^80}".format("Please type 1 to see the instructions,"))
        see_instructions = input("{:^80}".format("or 2 to skip them and start the game:\n"))
    # Take user to relevent page.
    if see_instructions == "1":
        instructions()
    else:
        play()


def instructions():
    """
    Clear terminal and show instructions
    """
    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # print instructions
    print("{:^80}".format("How to play:\n"))
    print("{:^80}".format("To play hangman, all you need to do is guess"))
    print("{:^80}".format("the word one letter at a time.\n"))
    print("{:^80}".format("1. Type a letter of your choice and hit enter.\n"))
    print("{:^80}".format("2. If your guess is correct the letter will"))
    print("{:^80}".format("show within the hidden word.\n"))
    print("{:^80}".format("3. If your guess is incorrect a section of the"))
    print("{:^80}".format("hangman picture will appear.\n"))
    print("{:^80}".format("4. Keep guessing until either you guess the"))
    print("{:^80}".format("correct word or you run out of tries.\n"))
    # Ask user if they are ready to play.
    print("{:^80}".format("Are you ready to play?"))
    ready = input("{:^80}".format("Please type 1 for yes and 2 for no:\n"))
    # Make sure users input is valid.
    while ready != "1" and ready != "2":
        print("{:^80}".format("Invalid input,"))
        ready = input("{:^80}".format("if you are ready press 1 if not press 2:\n"))
    # Take user to relevent page.
    if ready == "1":
        play()
    else:
        welcome()


def get_word():
    """
    Get word from words.py words list for user to guess.
    """
    word = random.choice(words)
    return word.upper()


def play():
    # clear termainal
    os.system('cls' if os.name == 'nt' else 'clear')
    # run game
    print("run")


welcome()


def hangman_img(tries):
    stages = [ """
                  --------
                  |      |
                  |      o
                  |    \\|/
                  |      |
                  |     /\\
                  ---
               """,
               """
                  --------
                  |      |
                  |      o
                  |    \\|/
                  |      |
                  |     /
                  ---
               """,
               """
                  --------
                  |      |
                  |      o
                  |    \\|/
                  |      |
                  |     
                  ---
               """,
               """
                  --------
                  |      |
                  |      o
                  |    \\|
                  |      |
                  |     
                  ---
               """,
               """
                  --------
                  |      |
                  |      o
                  |      |
                  |      |
                  |     
                  ---
               """,
               """
                  --------
                  |      |
                  |      o
                  |      
                  |      
                  |     
                  ---
               """,
               """
                  --------
                  |      |
                  |      
                  |      
                  |      
                  |     
                  ---
               """
    ]
    return stages[tries]