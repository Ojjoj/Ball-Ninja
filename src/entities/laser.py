import pygame
from src import settings

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.image.load(settings.laser_path).convert_alpha()
        self.current_height = 0
        self.max_height = y
        self.speed = settings.laser_speed
        self.width = settings.laser_width
        self.image = pygame.transform.scale(self.original_image, settings.laser_dimensions)
        self.rect = self.image.get_rect(midbottom=(x, y))

    def update(self):
        self.current_height += self.speed

        if self.current_height > self.max_height:
            self.kill()
            return

        self.image = pygame.transform.scale(self.original_image, (self.width, self.current_height))
        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
