from random import randint
from brain_games.logic import GLOBAL_COUNT, START, END
from brain_games.logic import name, logic_answer, logic_bye


# flake8: noqa: C901
def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_global = 0
    for i in range(GLOBAL_COUNT):
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

        print(f'Question: {num}')
        answer = input('Your answer: ')
        if logic_answer(answer, correct):
            count_global += 1
        else:
            count_global = 0
            break
    if count_global == 3:
        logic_bye(name)
