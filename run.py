"""
All imports.
"""
import os
import random
from words import words


def welcome():
    """
    Show welcome message and ask user if they would like to see instructions.
    """
    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
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
        see_instructions = input(
            "{:^80}".format("or 2 to skip them and start the game:\n")
        )
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
    os.system("cls" if os.name == "nt" else "clear")
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


def play():
    """
    Get word from words.py, ask user to guess a letter and compare results.
    """
    # write here ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    word = random.choice(words)
    tries = 6
    guessed = False
    guessed_letters = []
    word_letters = set(word)
    # Get word from words.py words list.
    print(word)
    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # test printing word. ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("{:^80}".format(word))
    # write here ~~~~~~~~~~~~~~~~~~~~~~
    while tries > 0 and guessed is False:
        # Display title
        print("{:-^80}".format("HANGMAN"))
        print("\n")
        # print letters user has guessed so far.
        print("{:^80}".format("You have used these letters so far:"))
        print("{:^80}".format(" ".join(guessed_letters)))
        print("\n")
        # Ask user to enter a letter.
        users_guess = input("{:^80}".format("Please enter a letter:\n")).upper()
        print("\n")
        # Print number of guesses left.
        print("{:^80}".format("Tries left = "))
        print("{:^80}".format(tries))
        print("\n")
        # Print guessed letters.
        print("{:^80}".format("letters revealed in word so far:"))
        reveal_word = "_" * len(word)
        print("{:^80}".format(reveal_word))
        print("\n")
        # write here.
        if len(users_guess) == 1 and users_guess.isalpha():
            if users_guess in guessed_letters:
                print("{:^80}".format("You already guessed"))
            elif users_guess not in word:
                print("{:^80}".format(users_guess))
                print("{:^80}".format("is not in the word, try again."))
                tries -= 1
                guessed_letters.append(users_guess)
            else:
                print("{:^80}".format("correct guess."))
                guessed_letters.append(users_guess)
        else:
            print("{:^80}".format("Invalid guess, letters only."))


welcome()
