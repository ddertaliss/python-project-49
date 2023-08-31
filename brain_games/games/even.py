from random import randint
from brain_games.games.consts import START, END


def main():
    quest = randint(START, END)
    if quest % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    return quest, correct


