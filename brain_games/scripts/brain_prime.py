from brain_games.logic import engine
from brain_games.games import prime
from brain_games.games.consts import STR_PRIME


def main():
    engine(prime, STR_PRIME)


if __name__ == '__main__':
    main()
