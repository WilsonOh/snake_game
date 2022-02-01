import random
import pygame


class Food:
    def __init__(self, game):
        self.x = 0
        self.y = 0
        self.game = game

    def spawn(self, snake):
        while True:
            self.x = random.randrange(0, self.game.WIDTH, self.game.SQ_SIZE)
            self.y = random.randrange(0, self.game.HEIGHT, self.game.SQ_SIZE)

            for block in snake.body:
                if self.x == block.x and self.y == block.y:
                    continue
            break

    def eaten(self, snake):
        if self.x == snake.body[0].x and self.y == snake.body[0].y:
            self.spawn(snake)
            snake.move(grow=True)

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.game.SQ_SIZE, self.game.SQ_SIZE)
        pygame.draw.rect(self.game.window, pygame.Color('red'), rect)




