from random import randint
def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        num = randint(1, 40)
        correct = None
        answer = None
        count = 1
        count_global = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            correct = 'yes'
        else:
            correct = 'no'
        
        print(f'Question: {num}')
        answer = input('Your answer: ')
        if answer == correct:
            print('Correct!')
            count_global += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct}.')
            print("Let's try again, {name}")
            count_global = 0
    if count_global == 3:
        print(f'Congratulations, {name}!')
