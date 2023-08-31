def welcome_user():
    name = input('May I have your name? ')
    print(f'Hello, {name}')
    return name


welcome_name = welcome_user()
if __name__ == '__main__':
    welcome_user()
