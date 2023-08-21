from random import randint
def main():
        print('Welcome to the Brain Games!')
        name = input('May I have your name? ')
        print(f'Hello, {name}')

        count = 0
        for i in range(3):
            fst_num = randint(1, 80)
            scnd_num = randint(1, 80)
            num1 = None
            num2 = None
            if fst_num < scnd_num:
                num1 = fst_num
                num2 = scnd_num
            else:
                num1 = scnd_num
                num2 = fst_num
            
            count_num = None 
            for j in range(1, num1 + 1):
                if num1 % j == 0 and num2 % j == 0:
                    correct_answer = j
                    if j == 1:
                        if fst_num % 2 == 0 and scnd_num % 2 == 0:
                            continue
                        else:
                            break

            print(f'Question: {fst_num} {scnd_num}')
            answer = input('Your answer: ')
            if int(correct_answer) == int(answer):
                print('Correct!')
                count += 1
                continue
            else:
                print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
                count = 0
                continue
        if count == 3:
             print(f'Congratulations, {name}!')
