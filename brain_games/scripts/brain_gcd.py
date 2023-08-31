from brain_games.logic import engine
from brain_games.games import gcd
from brain_games.games.consts import STR_GCD


def main():
    engine(gcd, STR_GCD)


if __name__ == '__main__':
    main()
