from Game import Game

WIDTH: int = 1200
HEIGHT: int = 1000
SQ_SIZE = 40


def main():
    game = Game(WIDTH, HEIGHT, SQ_SIZE)
    game.run()


if __name__ == '__main__':
    main()
