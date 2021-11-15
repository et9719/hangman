# Hangman

Hangman is a game usually played by two or more people, where one person thinks of a word while the others guess what the word is by guessing one letter at a time until the whole word is revealed.
For this project I wanted to create a version of this game that you can play against the computer rather than playing against another person.
This is done by using python to generate the word and check if the users guesses are correct, incorrect, invalid or if the user has already guessed the letter.


[Click here to go to the live website!](https://hang-the-guy.herokuapp.com/) 

<!-- Table of contents -->

<!-- plans and goals -->
<img src="images/flow.png" alt="Screenshot of the hangman flow chart">  

<!-- Features -->

<!-- Testing -->
### Python
Python was tested using PEP8 [PEP8 validator](http://pep8online.com/) 

The Python results came back with the following:

<img src="images/validate.png" alt="Screenshot of results">

- 7x line too long 

- To fix this I added a "\" within the print statements to shorten the lines while keeping the same text.
However, 1 out of the 7 lines that were too long was:
reveal_word = [letter if letter in guessed_letters else "_" for letter in word]
When trying to add "\" to this line it came back with more errors as this is between brackets and not just a string.

<img src="images/" alt="Add Screenshot of the new errors">  ~~~~~~~~~~~~~~~~~~~~~~~~~

### Manual Testing 


### Bugs 
1. I found that when a user guesses every letter in a word, the loop isn't ending meaning that if the user still has tries left even if they have guessed every letter it will keep asking them to enter another letter until the user runs out of tries. 

<img src="images/bug.png" alt="Screenshot of the bug">  

- fixed? 

- what did i do to fix it?

<!-- Deployment -->

<!-- Credits -->
flow chart - https://www.lucidchart.com/pages/
random word generator = https://randomwordgenerator.com/
code beautifier = https://codebeautify.org/python-formatter-beautifier
validator -http://pep8online.com/