import prompt
def welcome_user(name):
    print('May I have your name?')
    name = prompt.string('May I have your name? ' )
    print(f'Hello, {name}')
if __name__ == '__main__':
    welcome_user()

    
    
