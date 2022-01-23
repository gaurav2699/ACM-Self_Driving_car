import pygame
from pygame.locals import *
import time
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1400


class Obstacle:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("obstacle.png").convert()
        self.parent_screen = parent_screen
        random.seed()
        self.x = random.randint(2, 26) * 50
        self.y = random.randint(2, 13) * 50

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        random.seed()
        self.x = random.randint(2, 26) * 50
        self.y = random.randint(2, 13) * 50


class Car:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("car-cyan-resize(50).png").convert()
        self.direction = 'right'
        self.x = 0
        self.y = 50

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
            self.y -= 25

        if self.direction == 'down':
            self.y += 25

        if self.direction == 'right':
            self.x += 50
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.render_background()
        self.car = Car(self.surface)
        self.car.draw()
        self.obstacle = Obstacle(self.surface)
        self.obstacle.draw()
        self.obstacle2 = Obstacle(self.surface)
        self.obstacle2.draw()
        self.obstacle3 = Obstacle(self.surface)
        self.obstacle3.draw()
        self.obstacle4 = Obstacle(self.surface)
        self.obstacle4.draw()
        self.obstacle5 = Obstacle(self.surface)
        self.obstacle5.draw()

    def draw_grid(self):
        blockSize = 50  # Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.surface, WHITE, rect, 1)

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + 50:
            if y2 <= y1 < y2 + 50:  # here y will be same
                return True

        return False

    def render_background(self):
        bg = pygame.image.load("background-final.png")
        self.surface.blit(bg, (0, 0))

    def run(self):

        running = True

        while running:
            #self.draw_grid()
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
            try:
                self.play()
            except Exception as e:
                self.crashed()
                running = False

            time.sleep(0.2)

    def play(self):
        self.render_background()
        #self.draw_grid()
        self.car.walk()
        self.obstacle.draw()
        self.obstacle2.draw()
        self.obstacle3.draw()
        self.obstacle4.draw()
        self.obstacle5.draw()
        if self.is_collision(self.obstacle.x, self.obstacle.y, self.car.x, self.car.y):
            raise "Collision occurred"
        if self.is_collision(self.obstacle2.x, self.obstacle2.y, self.car.x, self.car.y):
            raise "Collision occurred"
        if self.is_collision(self.obstacle3.x, self.obstacle3.y, self.car.x, self.car.y):
            raise "Collision occurred"
        if self.is_collision(self.obstacle4.x, self.obstacle4.y, self.car.x, self.car.y):
            raise "Collision occurred"
        if self.is_collision(self.obstacle5.x, self.obstacle5.y, self.car.x, self.car.y):
            raise "Collision occurred"

    def crashed(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 60)
        line = font.render("CRASHED!", True, RED)
        self.surface.blit(line, (600, 350))
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
