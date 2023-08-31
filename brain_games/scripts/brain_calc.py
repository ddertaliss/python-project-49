from brain_games.logic import engine
from brain_games.games import calc
from brain_games.games.consts import STR_CALC

def main():
    engine(calc, STR_CALC)


if __name__ == '__main__':
    main()
