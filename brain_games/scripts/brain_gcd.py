from random import randint
from math import gcd
from brain_games.logic import GLOBAL_COUNT, START, END
from brain_games.logic import name, logic_answer, logic_bye


def main():
    count = 0
    for i in range(GLOBAL_COUNT):
        print('Find the greatest common divisor of given numbers.')
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

        print(f'Question: {fst_num} {scnd_num}')
        answer = int(input('Your answer: '))
        if logic_answer(answer, correct):
            count += 1
        else:
            count = 0
            break
    if count == 3:
        logic_bye(name)
