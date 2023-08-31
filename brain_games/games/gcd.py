from brain_games.games.consts import START, END
from random import randint
from math import gcd


def main():
    fst_num = randint(START, END)
    scnd_num = randint(START, END)
    num1 = None
    num2 = None
    if fst_num < scnd_num:
        num1 = fst_num
        num2 = scnd_num
    else:
        num1 = scnd_num
        num2 = fst_num

    correct = gcd(num1, num2)
    quest = f'{fst_num} {scnd_num}'
    return quest, correct
