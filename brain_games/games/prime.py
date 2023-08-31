from random import randint
from brain_games.games.consts import START, END


# flake8: noqa: C901
def main():
    count_global = 0
    num = randint(START, END)
    correct = None
    answer = None
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        correct = 'yes'
    else:
        correct = 'no'
    quest = str(num)
    return quest, correct