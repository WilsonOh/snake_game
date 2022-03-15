import pygame
from Snake import Snake
from Food import Food
from settings import *
from pause_screen import pause_screen
from directions import Direction


class Game:

    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Snake Game')
        self._clock = pygame.time.Clock()
        self._snake = Snake()
        self._food = Food()
        self._food.spawn(self._snake)

    def run(self):
        while True:
            self._event_handler()
            self._update_screen()
            self._handle__snake()
            self._handle__food()
            self._clock.tick(FPS)

    def _update_screen(self):
        self._window.fill(pygame.Color('aquamarine2'))
        if DRAW_GRID:
            self._draw_grid()
        self._snake.draw()
        self._food.draw()
        pygame.display.update()

    def _handle__snake(self):
        self._snake.move_or_grow()
        self._snake.cannibalize()

    def _handle__food(self):
        self._food.eaten(self._snake)

    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.WINDOWMAXIMIZED:
                pygame.display.set_mode((MAXIMIZED_WINDOW_WIDTH, MAXIMIZED_WINDOW_HEIGHT), pygame.RESIZABLE)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self._snake.direction != Direction.DOWN:
            self._snake.direction = Direction.UP
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self._snake.direction != Direction.RIGHT:
            self._snake.direction = Direction.LEFT
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self._snake.direction != Direction.LEFT:
            self._snake.direction = Direction.RIGHT
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self._snake.direction != Direction.UP:
            self._snake.direction = Direction.DOWN
        if keys[pygame.K_ESCAPE]:
            pause_screen(len(self._snake.body) - SNAKE_INIT_LEN)

    def _draw_grid(self):
        for x in range(0, self._window.get_height(), SQ_SIZE):
            pygame.draw.line(self._window, pygame.Color('deeppink1'), (0, x), (self._window.get_width(), x))
        for y in range(0, self._window.get_width(), SQ_SIZE):
            pygame.draw.line(self._window, pygame.Color('deeppink1'), (y, 0), (y, self._window.get_height()))
