
from random import randint
from brain_games.logic import *
def main():

    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(GLOBAL_COUNT):
        num = randint(START, END)
        print(f'Question: {num}')
        correct = ''
        if num % 2 == 0:
            correct = 'yes'
        else:
            correct = 'no'
        answer = input('Your answer:')
        
        if logic_answer(answer, correct) == True:
            count += 1
        else:
            count = 0
            break
    if count == 3:
        logic_bye(name)
