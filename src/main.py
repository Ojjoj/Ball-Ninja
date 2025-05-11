import pygame
import sys

from src.entities.ball import Ball
from src import settings

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(settings.game_name)

background_image = pygame.image.load("assets/images/baalbek.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

ball = Ball(ball_type=1,  position=(400, 300))
ball_group = pygame.sprite.GroupSingle(ball)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))
    ball_group.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
