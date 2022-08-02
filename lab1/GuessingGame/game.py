from messages import *
from hiddenFunctions import *


"""
This is a simple guessing game written for COMPSCI 235 students to explore the debugging features of PyCharm.

Main Objective:
    Start by reading the code, running it, and playing a few games. 
    Question 1:     What is the probability of winning a game?
    Question 2:     Using the debugging feature, WITHOUT changing any code, it is possible to win every game.
                    What line did you insert the breakpoint at? 
    Question 3:     Using the debugging feature only, is it possible the user can win every game by guessing "42"?
    
Extension Activity:
    Extension 1.    This code is not very robust. If the player enters an incorrectly formatted 
                    guess (e.g. typing "seven") the code will crash.
                    Make the game more robust to user inputs (e.g. 
                    request another input if the user guesses outside the range).
    Extension 2.    You will find functions in numberChecker.py that check if the 
                    number is even or is a prime. First modify the game so that the 
                    computer and user can only select even numbers. Then modify the code so that 
                    the only prime numbers are used. Finally add an option to each round to select between using all
                    numbers, only even numbers, or only prime numbers.   
"""

gamesPlayed: int = 0
gamesWon: int = 0

def welcome():
    print(WELCOME)

def computer_pick_number():
    print(PICK_NUMBER)
    number = pickANumber()
    return number;

def user_guess(selected_number):
    guess = eval(input(PROMPT_GUESS))
    return guess

def endGame():
    print(final_score(gamesWon, gamesPlayed))


def game():
   global gamesWon, gamesPlayed
   print(LINE_OF_STARS)
   selected_number = computer_pick_number()
   guess = user_guess(selected_number)
   if selected_number == guess:
       print(WIN)
       gamesWon += 1
   else:
       print(LOSE)
   gamesPlayed += 1

def play_again():
    again = input(PLAY_AGAIN)
    if again != "y" and again != "n":
        print(INVALID_INPUT)
        play_again()

    elif again == "y":
        game()
        play_again()
    else:
        endGame()

def main():
    welcome()
    game()
    play_again()


main()