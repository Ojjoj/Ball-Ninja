import pygame
from abc import ABC, abstractmethod
from src import settings


class Stone(ABC, pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        original_image = pygame.image.load(settings.stone_path).convert_alpha()
        self.width, self.height = self.dimensions
        self.image = pygame.transform.scale(original_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=position)

    @property
    @abstractmethod
    def dimensions(self):
        pass


class Stone_1(Stone):
    @property
    def dimensions(self):
        return settings.stone_1_dimensions


class Stone_2(Stone):
    @property
    def dimensions(self):
        return settings.stone_2_dimensions


class Stone_3(Stone):
    @property
    def dimensions(self):
        return settings.stone_3_dimensions
