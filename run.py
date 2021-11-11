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
    print("HANGMAN".center(80, "-"))
    print("\n")
    print("Welcome to Hangman!\n\nBefore we start, would you like to see the\
 instructions or are you good to go?")
    # Ask user to choose if they want to see instructions or not.
    see_instructions = input("Please type 1 to see the instructions,or 2 for\
 good to go!:\n")
    # Make sure users input is valid.
    if see_instructions != "1" and see_instructions != "2":
        see_instructions = input("\nInvalid input, Please type 1 to see the\
 instructions, or 2 to skip them and start the game:\n")
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
    print("How to play:\n\nTo play hangman, all you need to do is guess the word\
 one letter at a time.\n\n1. Type a letter of your choice and hit enter.\n2. If\
 your guess is correct the letter will show within the hidden word.\n3. If your\
 guess is incorrect a section of the hangman picture will appear.\n4. Keep guessing\
 until either you guess the correct word or you run out of tries.\n")
    # Ask user if they are ready to play.
    print("Are you ready to play?")
    ready = input("Please type 1 for yes and 2 for no:\n")
    # Make sure users input is valid.
    if ready != "1" and ready != "2":
        ready = input("Invalid input, if you are ready press 1 if not press 2:\n")
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
    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # print title
    print("HANGMAN".center(80, "-"))
    print("\n")
    # write here ~~~~~~~~~~~~~~~~~~~~~~
    while tries > 0 and guessed is False:
        reveal_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(reveal_word))
        print("\n")
        # Ask user to enter a letter.
        users_guess = input("Please enter a letter:\n").upper()
        print("\n")
        # clear terminal
        os.system("cls" if os.name == "nt" else "clear")
        # write here.
        if len(users_guess) == 1 and users_guess.isalpha():
            if users_guess in guessed_letters:
                print("HANGMAN".center(80, "-"))
                print("\n")
                print("You already guessed ", users_guess, "\n")
                # print letters user has guessed so far.
                print("You have used these letters so far:")
                print(" ".join(guessed_letters))
                print("\n")
            elif users_guess not in word:
                print("HANGMAN".center(80, "-"))
                print("\n")
                print(users_guess, " is not in the word, try again.")
                tries -= 1
                print("Tries left = ", tries)
                print("\n")
                guessed_letters.append(users_guess)
                print("You have used these letters so far:")
                print(" ".join(guessed_letters))
                print("\n")
            else:
                print("HANGMAN".center(80, "-"))
                print("\n")
                print("Correct guess!\n")
                guessed_letters.append(users_guess)
                if "_" not in reveal_word:
                    guessed = True
                # print letters user has guessed so far.
                print("You have used these letters so far:")
                print(" ".join(guessed_letters))
                print("\n")
        else:
            print("HANGMAN".center(80, "-"))
            print("\n")
            print("Invalid guess, letters only.\n")
    if tries == 0:
        # clear terminal
        os.system("cls" if os.name == "nt" else "clear")
        # print title
        print("HANGMAN".center(80, "-"))
        print("\n")
        print("Your out of Tries :(")
        print("The word was", word, "\n")
        play_again = input("Would you like to play again?\nType 1 for Yes or 2 for No:\n").upper()
        # Make sure users input is valid.
        if play_again != "1" and play_again != "2":
            play_again = input("Invalid input, if you want to play again press 1 if not press 2:\n")
        # Take user to relevent page.
        if play_again == "1":
            play()
        else:
            # clear terminal
            os.system("cls" if os.name == "nt" else "clear")
            # print title
            print("HANGMAN".center(80, "-"))
            print("\n")
            print("Thanks for playing, goodBye!")
    if guessed is True:
        # clear terminal
        os.system("cls" if os.name == "nt" else "clear")
        # print title
        print("HANGMAN".center(80, "-"))
        print("\n")
        print("Congratualtions!\nYou guessed the word, You win!\n")
        play_again = input("Would you like to play again?\nType 1 for Yes or 2 for No:\n").upper()
        # Make sure users input is valid.
        if play_again != "1" and play_again != "2":
            play_again = input("Invalid input, if you want to play again press 1 if not press 2:\n")
        # Take user to relevent page.
        if play_again == "1":
            play()
        else:
            # clear terminal
            os.system("cls" if os.name == "nt" else "clear")
            # print title
            print("HANGMAN".center(80, "-"))
            print("\n")
            print("Thanks for playing, goodBye!")


welcome()
