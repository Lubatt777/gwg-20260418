from random import random


def who_win(winner):
    if winner == "Win":
        return f"{winner}, congrats"
    else:
        return f"{winner}, Try again"


def to_int(message):
    return int(message)


while True:

    """This is random number generator by bot 
    when user upper number from bot you win
    in opposite you lose. Please insert number when you insert
    text it will crash. Good luck
    """
    random_number = round(random()*10)
    message = input("USER: ")
    user_number = to_int(message)
    if random_number == user_number:
        win = who_win(winner="Tie")
        print(win)
    elif random_number > user_number:
        win = who_win(winner="Lose")
        print(win)
    else:
        win = who_win(winner="Win")
        print(win)
        break
