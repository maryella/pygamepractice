import pygame
from pygame.locals import *
import random

#defining some stuff
WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#start game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
#player = Player()
#all_sprites.add(player)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False


    all_sprites.update()

    screen.fill(BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()