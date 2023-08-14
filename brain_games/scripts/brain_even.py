from random import randint
from brain_games.cli import welcome_name
def main():
    def even():
            print('Welcome to the Brain Games!') 
            print('Answer "yes" if the number is even, otherwise answer "no".')
            num = randint(1, 30)
            print(f'Question: {num}')
            answer = input('Your answer:')
    
            correct_answer = ''
            if num % 2 == 0:
                correct_answer = 'yes'
            else:
                correct_answer = 'no'
            if answer == correct_answer:
                print('Correct!')
                return True
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}. Let's try again, {welcome_name}!")
                return False
    count = 0
    while count != 3:
        if even() == True:
            count += 1
        else:
            count = 0
            continue
    if count == 3:
        print(f'Congratulations, {welcome_name}!')

