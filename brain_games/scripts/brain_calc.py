from random import randint
from brain_games.logic import *
def main():
    logic_hello()
    print('What is the result of the expression?')

    count = 0
    for i in range(3):
        FST_START = 1
        FST_END = 30
        SCND_START = 2
        SCND_END = 31
        FST_OP = 0
        SCND_OP = 3
        fst_num = randint(FST_START, FST_END)
        scnd_num = randint(SCND_START, SCND_END)
        correct_answer = None
        op_string = ''
    #  '+' = 0, '-' = 1, '*' = 2
        operator = randint(FST_OP, SCND_OP)
        if operator == 0:
            correct_answer = fst_num + scnd_num
            op_string = '+'
        elif operator == 1:
            correct_answer = fst_num - scnd_num
            op_string = '-'
        else:
            correct_answer = fst_num * scnd_num
            op_string = '*'
        print(f'Question: {fst_num} {op_string} {scnd_num}')
        answer = int(input('Your answer: '))

        if logic_answer == True:
            count += 1
        else:
            count = 0
            continue
    if count == 3:
        logic_bye(name)
