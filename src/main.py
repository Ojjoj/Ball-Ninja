import pygame
import sys

from src.entities.ball import Ball, Ball_1
from src.entities.player import Player
from src import settings
from src.utils import graphics

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(settings.game_name)
clock = pygame.time.Clock()

background_image = pygame.image.load("assets/images/backgrounds/raouche.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
background_image = graphics.gaussian_blur(background_image, settings.blur_radius)

ground_image = pygame.image.load("assets/images/sprites/ground.png").convert()
ground_image = pygame.transform.scale(ground_image, (WIDTH, 80))

player = Player()
player_group = pygame.sprite.GroupSingle(player)

ball = Ball_1()
ball_group = pygame.sprite.GroupSingle(ball)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))
    screen.blit(ground_image, (0,HEIGHT - 80))

    keys = pygame.key.get_pressed()

    ball_group.update()
    player_group.update(keys)

    ball_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
    clock.tick(settings.fps)

pygame.quit()
sys.exit()
