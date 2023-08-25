from random import randint
from brain_games.logic import *
def main():
    print('What number is missing in the progression?')

    count = 0
    for i in range(3):
        FST_START = 2
        FST_END = 4
        SCND_START = 15
        SCND_END = 25
        fst_num = randint(FST_START, FST_END)
        scnd_num = randint(SCND_START, SCND_END)
        diff = 2
        matrix = []
        for j in range(fst_num, scnd_num, diff):
            matrix.append(j)
        rndm_ind = randint(1, len(matrix) - 1)
        correct = matrix.copy()
        correct = correct[rndm_ind]
        question = matrix
        question[rndm_ind] = '..'
        print_question = [str(i) for i in question]

        print('Question: ', end = '')
        print(*print_question)
        answer = int(input('Your answer: '))
        if logic_answer(answer, correct) == True:
            count += 1
        else:
            count = 0
            break
    if count == 3:
        logic_bye(name)
