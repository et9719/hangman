# Hangman

Hangman is a game usually played by two or more people, where one person thinks of a word while the others guess what the word is by guessing one letter at a time until the whole word is revealed.
For this project I wanted to create a version of this game that you can play against the computer rather than playing against another person.
This is done by using python to generate the word and check if the users guesses are correct, incorrect, invalid or if the user has already guessed the letter.


[Click here to go to the live website!](https://hang-the-guy.herokuapp.com/) 

## Table of contents 

1. [Plans and structure](#plans-and-structure)
2. [Features](#features)
    - [](#)
    - [](#)
    - [](#)
    - [](#)    
3. [Testing](#testing)
    - [Python](#python)
    - [Manual Testing](#manual-testing)
    - [Bugs ](#bugs)
4. [Deployment](#deployment)
5. [Finished product](#finished-product)
6. [Credits](#credits)
    
## Plans and structure 

<img src="images/flow.png" alt="Screenshot of the hangman flow chart">  

Throughout the process of making this project I decided to change a couple of things due to the time limmit i had to make the game. 

- Originally I planned to have 2 levels easy and hard so the user could choose the level of difficaulty they would like to play.
- I had also planned to have a visable image of hangman being shown so the user could see how many lives they had left until the game was over. 

I decided that these two things were not as important as all the other functions so I would like to either implement them if i have time to at the end of the process or if not I would like to impliment them in the future so I can continue to use this game with family and friends. 


## Features 

<!-- Add features section -->

## Testing

### Python
Python was tested using PEP8 [PEP8 validator](http://pep8online.com/) 

The Python results came back with the following:

<img src="images/validate.png" alt="Screenshot of results">

- 7x line too long 

- To fix this I added a "\" within the print statements to shorten the lines while keeping the same text.
However, 1 out of the 7 lines that were too long was:
reveal_word = [letter if letter in guessed_letters else "_" for letter in word]
When trying to add "\" to this line it came back with more errors as this is between brackets and not just a string.

<img src="images/valid.png" alt="Screenshot of the new errors"> ~~~~~~~~~~~~~~~~~~~

### Manual Testing 

1. Would the user like to see the instructions?
 the user is asked to input either 1 for yes or 2 for no. 

 - First I tested what would happen if the user typed anything other than 1 or 2: Error message shows, results were as expected.

 <img src="images/see-inst-invalid.png" alt="Screenshot of invalid input"> 

 - Next I tested what would happen if the user typed 1: Shows instructions, results were as expected.

 <img src="images/see-inst-1.png" alt="image of what happens when user types 1">

 - Last I tested what would happen if the user typed 2: Game starts,results were as expected.

 <img src="images/see-inst-2.png" alt="image of what happens when user types 2"> 

2. After reading the instructions the user is asked if they are ready to play, 1 for yes and 2 for no.

 - First I tested what would happen if the user typed anything other than 1 or 2: Error message shows, results were as expected.
 
 <img src="images/ready-invalid.png" alt="screenshot of invalid input"> 

 - Next I tested what would happen if the user typed 1: Game starts, results were as expected.

 <img src="images/ready-1.png" alt="image of what happens when user types 1">

 - Last I tested what would happen if the user typed 2: User us sent back to welcome page, results were as expected.

 <img src="images/ready-2.png" alt="image of what happens when user types 2"> 

3. Once game has started the user is asked to enter a letter.

 - First I tested what would happen if the user typed anything other a letter: Error message shows, results were as expected.
 
 <img src="images/game-invalid.png" alt="screenshot of invalid input"> 

 - Next I tested what would happen if the user typed a valid yet incorrect guess: Try again message shows and tries are appended, results were as expected.

 <img src="images/game-incorrect.png" alt="image of what happens when users guess is incorrect">

 - Then I tested what would happen if the user typed a correct guess: correct letter is put into place in the word, results were as expected.

 <img src="images/game-correct.png" alt="image of what happens when users guess is correct"> 

 - Last I tested what would happen if the user typed a letter they had already guessed: You have already guessed that letter message shows, results were as expected.
 
 <img src="images/game-repeat.png" alt="image of what happens when users guess is repeated"> 

4. At the end of the game the user is asked if they want to play again, 1 for yes 2 for no.
 
 - First I tested what would happen if the user typed anything other than 1 or 2: Error message shows, results were as expected.

 <img src="images/again-invalid.png" alt="Screenshot of invalid input"> 

 - Next I tested what would happen if the user typed 1: Game starts again, results were as expected.

 <img src="images/again-1.png" alt="image of what happens when user types 1">

 - Last I tested what would happen if the user typed 2: Goodbye message shows, results were as expected.

 <img src="images/again-2.png" alt="image of what happens when user types 2"> 

### Bugs 
1. I found that when a user guesses every letter in a word, the loop isn't ending meaning that if the user still has tries left even if they have guessed every letter it will keep asking them to enter another letter until the user runs out of tries. 

<img src="images/bug.png" alt="Screenshot of the bug">  

- fixed? 

- what did i do to fix it?

## Deployment 

<!-- Add Deployment -->

## Finished product

<!-- Add finished product -->

## Credits 
flow chart - https://www.lucidchart.com/pages/
random word generator = https://randomwordgenerator.com/
code beautifier = https://codebeautify.org/python-formatter-beautifier
validator -http://pep8online.com/