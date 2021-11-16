"""
All imports.
"""
import os
import random
from words import words


def title():
    """
    Print hangman title.
    """
    print("\033[1;36;40m")
    print("HANGMAN".center(80, "-"))
    print("\n")


def welcome():
    """
    Show welcome message and ask user if they would like to see instructions.
    """
    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # Welcome message.
    title()
    print("Welcome to Hangman!\n\nBefore we start, would you like to see the\
 instructions or are you good to go?")
    # Ask user to choose if they want to see instructions or not.
    see_instructions = input("Please type 1 to see the instructions,or 2 for\
 good to go!:\n")
    # Make sure users input is valid.
    while see_instructions != "1" and see_instructions != "2":
        see_instructions = input("\n\033[1;31;40mInvalid input, Please type 1 to see the\
 instructions, or 2 to skip them and start the game:\n")
    # Take user to relevent page.
    if see_instructions == "1":
        instructions()
    else:
        play()


def instructions():
    """
    Show instructions and ask if user is ready to play.
    """
    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # print instructions
    print("\033[1;36;40mHow to play:\n\nTo play hangman, all you need to\
 do is guess the word one letter at a time.\n\n1. Type a letter of your\
 choice and hit enter.\n2. If your guess is correct the letter will show\
 within the hidden word.\n3. If your guess is incorrect a section of the\
 hangman picture will appear.\n4. Keep guessing until either you guess\
 the correct word or you run out of tries.\n")
    # Ask user if they are ready to play.
    print("Are you ready to play?")
    ready = input("Please type 1 for yes and 2 for no:\n")
    # Make sure users input is valid.
    while ready != "1" and ready != "2":
        ready = input("\n\033[1;31;40mInvalid input, if you are ready\
 press 1 if not press 2:\n")
    # Take user to relevent page.
    if ready == "1":
        play()
    else:
        welcome()


def play_again():
    """
    Ask user if they would like to play the game again.
    """
    play_again_q = input("\033[1;36;40mWould you like to play\
 again?\nType 1 for Yes or 2 for No:\n")
    # Make sure users input is valid.
    while play_again_q != "1" and play_again_q != "2":
        play_again_q = input("\n\033[1;31;40mInvalid input, if you want\
 to play again press 1 if not press 2:\n")
    # Take user to relevent page.
    if play_again_q == "1":
        play()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        title()
        print("Thanks for playing, goodBye!")


def play():
    """
    Get word from words.py, ask user to guess a letter and compare results.
    """
    word = random.choice(words)
    tries = 6
    guessed = False
    guessed_letters = []
    # Clear terminal and print title
    os.system("cls" if os.name == "nt" else "clear")
    title()
    # Compare users guess to word.
    while tries > 0 and guessed is False:
        reveal_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("\033[1;36;40m")
        print(" ".join(reveal_word))
        print("\n")
        # Ask user to enter a letter.
        users_guess = input("Please enter a letter:\n").upper()
        print("\n")
        # Clear terminal
        os.system("cls" if os.name == "nt" else "clear")
        # If users guess is valid input:
        if len(users_guess) == 1 and users_guess.isalpha():
            # If the user has already guessed this letter:
            if users_guess in guessed_letters:
                title()
                print("\033[1;31;40mYou already guessed ", users_guess, "\n")
                print("\033[1;36;40mYou have used these letters so far:")
                print(" ".join(guessed_letters))
                print("\n")
            # If the users guess is not in the word:
            elif users_guess not in word:
                title()
                print("\033[1;31;40m", users_guess, " is not in\
 the word, try again.")
                tries -= 1
                print("\033[1;36;40mTries left = ", tries)
                print("\n")
                guessed_letters.append(users_guess)
                print("You have used these letters so far:")
                print(" ".join(guessed_letters))
                print("\n")
            # If the user guesses a correct letter:
            else:
                title()
                print("\033[1;32;40mCorrect guess!\n")
                guessed_letters.append(users_guess)
                print("\033[1;36;40mYou have used these letters so far:")
                print(" ".join(guessed_letters))
                print("\n")
                if "_" not in reveal_word:
                    guessed = True
        # If users input is not valid:
        else:
            title()
            print("\n\033[1;31;40mInvalid guess, letters only.\n")
    # If the user wins and gets the whole word:
    if guessed is True:
        os.system("cls" if os.name == "nt" else "clear")
        title()
        print("Congratualtions!\nYou guessed the word, You win!\n")
        play_again()
    # If the user runs out of tries:
    else:
        os.system("cls" if os.name == "nt" else "clear")
        title()
        print("\033[1;31;40mYour out of Tries :(")
        print("The word was", word, "\n")
        play_again()


welcome()
