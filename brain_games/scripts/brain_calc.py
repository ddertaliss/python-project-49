from random import randint
def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')

    count = 0
    for i in range(3):
        fst_num = randint(1, 30)
        scnd_num = randint(2, 31)
        correct_answer = None
        op_string = ''
    #  '+' = 0, '-' = 1, '*' = 2
        operator = randint(3)
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
        answer = input('Your answer: ')

        if correct_answer == answer:
            count += 1
            print('Correct!')
            continue
        else:
            count = 0
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            continue
    if count == 0:
        print(f'Congratulations, {name}')
