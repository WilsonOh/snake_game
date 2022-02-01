import pygame
from Snake import Snake
from Food import Food
from enum import Enum, auto


class Game:

    class Direction(Enum):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

    WIDTH = 0
    HEIGHT = 0
    SQ_SIZE = 0
    FPS = 15
    window = None
    clock = pygame.time.Clock()
    snake = None
    snake_init_len = 3
    food = None

    def __init__(self, width, height, sq_size):
        self.WIDTH = width
        self.HEIGHT = height
        self.SQ_SIZE = sq_size
        self.SQ_WIDTH = self.WIDTH/self.SQ_SIZE
        self.SQ_HEIGHT = self.HEIGHT/self.SQ_SIZE

    def run(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Snake Game')
        self.snake = Snake(self.snake_init_len, self)
        self.food = Food(self)
        self.food.spawn(self.snake)
        while True:
            self.clock.tick(self.FPS)
            self.event_handler()
            self.draw_window()
            self.snake.move()
            self.snake.cannibalize()
            self.food.eaten(self.snake)
            self.food.draw()
            self.snake.draw()
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.WINDOWMAXIMIZED:
                pygame.display.set_mode((2520, 1360), pygame.RESIZABLE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.snake.direction != self.Direction.DOWN:
            self.snake.direction = self.Direction.UP
        if keys[pygame.K_a] and self.snake.direction != self.Direction.RIGHT:
            self.snake.direction = self.Direction.LEFT
        if keys[pygame.K_d] and self.snake.direction != self.Direction.LEFT:
            self.snake.direction = self.Direction.RIGHT
        if keys[pygame.K_s] and self.snake.direction != self.Direction.UP:
            self.snake.direction = self.Direction.DOWN
        if keys[pygame.K_ESCAPE]:
            self.pause_game()

    def draw_window(self):
        self.window.fill(pygame.Color('white'))
        for x in range(0, self.window.get_height(), self.SQ_SIZE):
            pygame.draw.line(self.window, pygame.Color('grey'), (0, x), (self.window.get_width(), x))
        for y in range(0, self.window.get_width(), self.SQ_SIZE):
            pygame.draw.line(self.window, pygame.Color('grey'), (y, 0), (y, self.window.get_height()))

    def pause_game(self):
        clock = pygame.time.Clock()
        paused = True
        font = pygame.font.SysFont("comicsans", self.window.get_height()//15, bold=True)
        game_over_font = font.render(f"GAME PAUSED. YOUR SCORE IS {len(self.snake.body) - 3}",
                                     True, pygame.Color('red'))
        keys_font = font.render("Press escape to return or q to quit", True, pygame.Color('blue'))
        while paused:
            clock.tick(5)
            self.window.fill(pygame.Color('white'))
            self.window.blit(game_over_font, (self.window.get_width()//2 - game_over_font.get_width()//2,
                                              self.window.get_height()//2 - game_over_font.get_height()//2))
            self.window.blit(keys_font, (self.window.get_width()//2 - keys_font.get_width()//2,
                                         self.window.get_height()//2 - keys_font.get_height()//2 +
                                         game_over_font.get_height()))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

            pygame.display.update()
