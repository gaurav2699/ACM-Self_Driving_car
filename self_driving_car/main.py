import pygame
from pygame.locals import *
import time

# import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1400


class Car:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("car-cyan-resize(50).png").convert()
        self.direction = 'right'
        self.x = 0
        self.y = 25

    def draw(self):
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        if self.direction == 'up':
            self.y -= 50

        if self.direction == 'down':
            self.y += 50

        if self.direction == 'right':
            self.x += 50
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.surface.fill(BLACK)
        self.car = Car(self.surface)
        self.car.draw()

    def draw_grid(self):
        blockSize = 50  # Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.surface, WHITE, rect, 1)

    def run(self):

        running = True

        while running:
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.car.move_down()
                    if event.key == K_UP:
                        self.car.move_up()
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
                else:
                    self.car.move_right()
            self.play()

            time.sleep(1)

    def play(self):
        self.surface.fill(BLACK)
        self.draw_grid()
        self.car.walk()
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
