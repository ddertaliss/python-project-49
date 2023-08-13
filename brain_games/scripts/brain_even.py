from random import randint
from brain_games.cli import welcome_user.name
def main():
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
    else:
        print(f"{answer}is wrong answer ;(. Correct answer was {correct_answer}. Let's try again, {name}!")
main()
