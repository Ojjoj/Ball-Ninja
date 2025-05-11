import pygame

from src import settings


class Ball(pygame.sprite.Sprite):
    def __init__(self, position, ball_type):
        super().__init__()

        ball_path = settings.ball_path
        original_image = pygame.image.load(ball_path).convert_alpha()

        self.dimensions = self.set_dimensions()
        self.score = self.set_score()
        self.ball_type = ball_type
        self.image = pygame.transform.scale(original_image, self.dimensions)
        self.rect = self.image.get_rect(center=position)

    def set_dimensions(self):
        if self.ball_type == 1:
            return settings.ball_1_dimensions
        return None
        # TODO: more types

    def set_score(self):
        match self.ball_type:
            case 1:
                return settings.ball_1_score
            case 2:
                return settings.ball_1_score
        return None

Ball(1, )
        # TODO: more types
