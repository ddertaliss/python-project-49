from random import randint
def main():
        print('Welcome to the Brain Games!')
        name = input('May I have your name? ')
        print(f'Hello, {name}')
        print('Answer "yes" if the number is even, otherwise answer "no".')

        count = 0
        for _ in range(3):
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
                count += 1
                if count != 3:
                     continue
                else:
                     print(f"Congratulations, {name}!")
                     break

