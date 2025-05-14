import pygame
import sys

from src.entities.ball import Ball_1
from src.entities.player import Player
from src.entities.laser import Laser
from src import settings
from src.utils import graphics


pygame.init()

screen = pygame.display.set_mode(settings.screen_dimensions)
pygame.display.set_caption(settings.game_name)
clock = pygame.time.Clock()

background_image = pygame.image.load(settings.level_1_background_path).convert()
background_image = pygame.transform.scale(background_image, settings.screen_dimensions)
background_image = graphics.gaussian_blur(background_image, settings.blur_radius)

ground_image = pygame.image.load(settings.ground_path).convert()
ground_image = pygame.transform.scale(ground_image, (settings.screen_width, 80))

player = Player()
player_group = pygame.sprite.GroupSingle(player)

ball = Ball_1(settings.ball_1_position)
ball_group = pygame.sprite.GroupSingle(ball)

laser_group = pygame.sprite.Group()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(laser_group) == 0:
                    x = player.rect.centerx
                    y = settings.ground_y
                    laser = Laser(x, y)
                    laser_group.add(laser)

    screen.blit(background_image, (0, 0))
    screen.blit(ground_image, (0, settings.screen_height - 80))

    keys = pygame.key.get_pressed()

    ball_group.update()
    laser_group.update()
    player_group.update(keys)

    ball_group.draw(screen)
    laser_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
    clock.tick(settings.fps)

pygame.quit()
sys.exit()
