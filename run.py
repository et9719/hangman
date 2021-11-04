import random
from words import words

def welcome():
    """
    Show welcome message and ask user if they would like to see instructions.
    """
    print("{:-^45}".format("HANGMAN"))
    print("\n")
    print("{:^45}".format("Welcome to Hangman!\n"))
    print("{:^45}".format("Before we start, would you like to see "))
    print("{:^45}".format("the instructions or are you good to go?\n"))
    print("{:^45}".format("Please type 1 to see the instructions,"))
    
    see_instructions = input("{:^45}".format("or 2 for good to go!: \n"))
    
    if see_instructions == "1":
        print("Instructions")
    else:
        print("Start game")


# def get_word():
#     """
#     Get word from words.py words list for user to guess.
#     """
#     word = random.choice(words)
#     return word.upper()
    
welcome()