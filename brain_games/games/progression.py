from random import randint

FST_START = 2
FST_END = 4
SCND_START = 15
SCND_END = 25
diff = 2


def main():
    fst_num = randint(FST_START, FST_END)
    scnd_num = randint(SCND_START, SCND_END)
    matrix = []
    for j in range(fst_num, scnd_num, diff):
        matrix.append(j)
    rndm_ind = randint(1, len(matrix) - 1)
    correct = matrix.copy()
    correct = correct[rndm_ind]
    question = matrix
    question[rndm_ind] = '..'
    list_quest = [str(i) for i in question]
    quest = ' '.join(list_quest)
    return quest, str(correct)
