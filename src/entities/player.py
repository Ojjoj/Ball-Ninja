import pygame

from src import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        player_path = settings.player_path
        original_image = pygame.image.load(player_path).convert_alpha()

        self.image = pygame.transform.scale(original_image, settings.player_dimensions)
        self.rect = self.image.get_rect(midbottom=position)
