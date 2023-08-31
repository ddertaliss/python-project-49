def engine(game, STRING):
    GLOBAL_COUNT = 3
    START = 1
    END = 80
    count = 0

    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    hello = (f'Hello, {name}!')
    print(hello)
    print(STRING)
    for _ in range(GLOBAL_COUNT):
        quest, correct = game.main()
        print(f'Question: {quest}')
        answer = input('Your answer: ')
        if answer == correct:
            print('Correct!')
            count += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct}.')
            print(f"Let's try again, {name[7:-1]}!")
            count = 0
            break
    if count == 3:
        print(f'Congratulations, {name[7:-1]}!')