from brain_games.games.consts import FST_START, FST_END, SCND_START
from brain_games.games.consts import SCND_END, FST_OP, SCND_OP
from random import randint


def main():
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
    quest = f'{fst_num} {op_string} {scnd_num}'
    return quest, str(correct)
