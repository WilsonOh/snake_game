from pygame import Rect
import pygame
import random


class Snake:
    def __init__(self, start_len, game):
        self.body = []
        self.game = game
        self.init_body(start_len)
        self.direction = random.choice(list(game.Direction))
        self.game_over = False

    def init_body(self, start_len):
        for i in range(start_len):
            self.body.append(
                Rect(((self.game.SQ_WIDTH // 2) - i) * self.game.SQ_SIZE,
                     (self.game.SQ_HEIGHT // 2) * self.game.SQ_SIZE,
                     self.game.SQ_SIZE, self.game.SQ_SIZE))

    def move(self, grow=False):
        new = Rect(self.body[0].x, self.body[0].y, self.game.SQ_SIZE, self.game.SQ_SIZE)
        if self.direction == self.game.Direction.UP:
            if self.body[0].y < 0:
                new.update(new.x, self.game.window.get_height(), self.game.SQ_SIZE, self.game.SQ_SIZE)
            new = new.move(0, -self.game.SQ_SIZE)
        if self.direction == self.game.Direction.DOWN:
            if self.body[0].y > self.game.window.get_height() - self.game.SQ_SIZE:
                new.update(new.x, -self.game.SQ_SIZE, self.game.SQ_SIZE, self.game.SQ_SIZE)
            new = new.move(0, self.game.SQ_SIZE)
        if self.direction == self.game.Direction.RIGHT:
            if self.body[0].x > self.game.window.get_width() - self.game.SQ_SIZE:
                new.update(-self.game.SQ_SIZE, new.y, self.game.SQ_SIZE, self.game.SQ_SIZE)
            new = new.move(self.game.SQ_SIZE, 0)
        if self.direction == self.game.Direction.LEFT:
            if self.body[0].x < 0:
                new.update(self.game.window.get_width(), new.y, self.game.SQ_SIZE, self.game.SQ_SIZE)
            new = new.move(-self.game.SQ_SIZE, 0)
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
                pygame.draw.rect(self.game.window, pygame.Color('purple'), block)
            else:
                pygame.draw.rect(self.game.window, pygame.Color('green'), block)
