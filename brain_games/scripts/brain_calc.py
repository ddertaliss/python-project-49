from random import randint
from brain_games.logic import GLOBAL_COUNT, name, logic_answer, logic_bye


def main():
    print('What is the result of the expression?')

    count = 0
    for i in range(GLOBAL_COUNT):
        FST_START = 1
        FST_END = 30
        SCND_START = 2
        SCND_END = 31
        FST_OP = 0
        SCND_OP = 3
        fst_num = randint(FST_START, FST_END)
        scnd_num = randint(SCND_START, SCND_END)
        correct = None
        op_string = ''
    #  '+' = 0, '-' = 1, '*' = 2
        operator = randint(FST_OP, SCND_OP)
        if operator == 0:
            correct = fst_num + scnd_num
            op_string = '+'
        elif operator == 1:
            correct = fst_num - scnd_num
            op_string = '-'
        else:
            correct = fst_num * scnd_num
            op_string = '*'
        print(f'Question: {fst_num} {op_string} {scnd_num}')
        answer = int(input('Your answer: '))

        if logic_answer(answer, correct):
            count += 1
        else:
            count = 0
            break
    if count == 3:
        logic_bye(name)
