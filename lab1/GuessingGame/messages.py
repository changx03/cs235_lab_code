WELCOME = "Welcome to the guessing game! \nI'm going to pick a number, and if you can guess it you win! \nIf you guess wrong, YOU LOSE!"
WIN = "Wow, lucky guess!!"
LOSE = "Haha, you lose!"
PICK_NUMBER = "Let's play!\nI'm thinking of a number... got it."
PROMPT_GUESS = "Now your turn to guess!\nEnter a number between 1 and 100: "
PLAY_AGAIN = "Would you like to play again? (Type 'y' for yes or  'n' for no.): "
INVALID_INPUT = "That is not a valid answer..."
LINE_OF_STARS = "**************************************"

def final_score(gamesWon, gamesPlayed):
    final_score_message = "Game over!\nYou won " + str(gamesWon) + " out of " + str(gamesPlayed) + " games."
    if gamesWon == gamesPlayed:
        final_score_message += "\nThat's improbable! Are you cheating??"
    return final_score_message
