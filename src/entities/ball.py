import pygame

from src import settings


class Ball(pygame.sprite.Sprite):
    def __init__(self, position, ball_type):
        super().__init__()

        ball_path = settings.ball_path
        original_image = pygame.image.load(ball_path).convert_alpha()

        self.ball_type = ball_type
        self.dimensions = self.set_dimensions()
        self.score = self.set_score()
        self.image = pygame.transform.scale(original_image, self.dimensions)
        self.rect = self.image.get_rect(center=position)

        self.x, self.y = float(self.rect.centerx), float(self.rect.centery)
        self.x_speed = settings.ball_1_initial_speed_x
        self.y_speed = settings.ball_1_initial_speed_y

    def set_dimensions(self):
        match self.ball_type:
            case 1:
                return settings.ball_1_dimensions
            case _:
                return None
        # TODO: more types

    def set_score(self):
        match self.ball_type:
            case 1:
                return settings.ball_1_score
            case 2:
                return settings.ball_1_score
            case _:
                return None

    def update(self):
        # apply gravity
        self.y_speed += settings.gravity

        # move
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.center = (int(self.x), int(self.y))

        # bounce off floor
        floor_y = settings.ground_y - self.dimensions[1] / 2
        if self.y >= floor_y and self.y_speed > 0:
            self.y = floor_y
            self.y_speed *= -settings.elasticity

        # bounce off ceiling
        ceil_y = settings.wall_thickness / 2 + self.dimensions[1] / 2
        if self.y <= ceil_y and self.y_speed < 0:
            self.y = ceil_y
            self.y_speed *= -settings.elasticity

        # bounce off left wall
        left_x = settings.wall_thickness / 2 + self.dimensions[0] / 2
        if self.x <= left_x and self.x_speed < 0:
            self.x = left_x
            self.x_speed *= -settings.elasticity

        # bounce off right wall
        right_x = settings.screen_width - settings.wall_thickness / 2 - self.dimensions[0] / 2
        if self.x >= right_x and self.x_speed > 0:
            self.x = right_x
            self.x_speed *= -settings.elasticity
