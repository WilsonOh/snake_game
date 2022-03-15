import random
import pygame
from settings import *


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.window = pygame.display.get_surface()

    def spawn(self, snake):
        while True:
            self.x = random.randrange(0, self.window.get_width(), SQ_SIZE)
            self.y = random.randrange(0, self.window.get_height(), SQ_SIZE)

            for block in snake.body:
                if self.x == block.x and self.y == block.y:
                    continue
            break

    def eaten(self, snake):
        if self.x == snake.body[0].x and self.y == snake.body[0].y:
            self.spawn(snake)
            snake.move_or_grow(grow=True)

    def draw(self):
        rect = pygame.Rect(self.x, self.y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(self.window, pygame.Color('red'), rect)
