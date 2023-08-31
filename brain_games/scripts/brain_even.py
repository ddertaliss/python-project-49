from brain_games.logic import engine
from brain_games.games import even
from brain_games.games.consts import STR_EVEN


def main():
    engine(even, STR_EVEN)


if __name__ == '__main__':
    main()
