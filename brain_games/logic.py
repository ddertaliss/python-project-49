GLOBAL_COUNT = 3
START = 1
END = 80
def logic_hello():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    hello = (f'Hello, {name}!')
    return hello

name = logic_hello()


def logic_answer(answer, correct):
    if answer == correct:
        print('Correct!')
        return True
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {correct}.')
        print(f"Let's try again, {name}")
        return False
    
    
def logic_bye(name):
    print(f'Congratulations, {name[7:-1]}!')
    
if __name__ == '__main__':
    logic_hello()
    logic_answer()
    logic_bye()
    
