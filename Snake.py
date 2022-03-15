from pygame import Rect
import pygame
import random
from settings import *
from directions import Direction


class Snake:
    def __init__(self):
        self.body = []
        self.init_body()
        self.direction = random.choice(list(Direction))
        self.window = pygame.display.get_surface()

    def init_body(self):
        for i in range(SNAKE_INIT_LEN):
            self.body.append(
                Rect(((SQ_WIDTH // 2) - i) * SQ_SIZE,
                     (SQ_HEIGHT // 2) * SQ_SIZE,
                     SQ_SIZE, SQ_SIZE))

    def move_or_grow(self, grow=False):
        window_rect = self.window.get_rect()
        new = Rect(self.body[0].x, self.body[0].y, SQ_SIZE, SQ_SIZE)
        match self.direction:
            case Direction.UP:
                if self.body[0].y < 0:
                    new.top = window_rect.bottom
                new.move_ip(0, -SQ_SIZE)
            case Direction.DOWN:
                if self.body[0].y > window_rect.height - SQ_SIZE:
                    new.bottom = window_rect.top
                new.move_ip(0, SQ_SIZE)
            case Direction.RIGHT:
                if self.body[0].x > window_rect.width - SQ_SIZE:
                    new.right = window_rect.left
                new.move_ip(SQ_SIZE, 0)
            case Direction.LEFT:
                if self.body[0].x < 0:
                    new.left = window_rect.right
                new.move_ip(-SQ_SIZE, 0)
        self.body.insert(0, new)
        if not grow:
            self.body.pop()

    def cannibalize(self):
        for idx, block in enumerate(self.body[1:]):
            if self.body[0].x == block.x and self.body[0].y == block.y:
                self.body = self.body[:idx]

    def draw(self):
        for idx, block in enumerate(self.body):
            if idx == 0:
                pygame.draw.rect(self.window, pygame.Color('purple'), block)
            else:
                pygame.draw.rect(self.window, pygame.Color('burlywood4'), block)
