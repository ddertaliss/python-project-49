from random import randint
def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    count = 0
    for i in range(3):
        fst_num = randint(1, 5)
        scnd_num = randint(15, 25)
        diff = 2
        matrix = []
        for j in range(fst_num, scnd_num, diff):
            matrix.append(j)
        rndm_ind = randint(1, len(matrix) - 1)
        correct = matrix.copy()
        correct = correct[rndm_ind]
        question = matrix
        question[rndm_ind] = '..'
        
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if int(correct) == int(answer):
            print('Correct!')
            count += 1

        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct}.')
            print(f"Let's try again, {name}!")
            count = 0
    if count == 3:
        print(f'Congratulations, {name}!')
