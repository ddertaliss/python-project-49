from random import randint
from brain_games.logic import *
def main():

        count = 0
        for i in range(3):
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
            
            count_num = None 
            correct = None
            for j in range(1, num1 + 1):
                if num1 % j == 0 and num2 % j == 0:
                    correct = j
                    if j == 1:
                        if fst_num % 2 == 0 and scnd_num % 2 == 0:
                            continue
                        else:
                            break

            print(f'Question: {fst_num} {scnd_num}')
            answer = int(input('Your answer: '))
            if logic_answer(answer, correct) == True:
                 count += 1
            else:
                 count = 0
                 break
        if count == 3:
            logic_bye(name)
