from brain_games.logic import engine
from brain_games.games import progression
from brain_games.games.consts import STR_PROGRESSION


def main():
    engine(progression, STR_PROGRESSION)


if __name__ == '__main__':
    main()
