import pygame

from abc import ABC, abstractmethod

from src import settings
from src.utils import physics
from src.utils.movement import Direction


class Ball(ABC, pygame.sprite.Sprite):
    def __init__(self, position, direction=Direction.RIGHT):
        super().__init__()
        self.direction = direction
        ball_path = settings.ball_path
        original_image = pygame.image.load(ball_path).convert_alpha()
        self.width, self.height = self.dimensions
        self.image = pygame.transform.scale(original_image, (self.width, self.height))
        self.position = position
        self.rect = self.image.get_rect(center=self.position)
        self.x, self.y = float(self.rect.centerx), float(self.rect.centery)
        self.x_speed, self.y_speed = self.initial_speed
        self.x_speed *= self.direction
        self.initial_y_speed = abs(self.y_speed)

    @property
    @abstractmethod
    def dimensions(self):
        pass

    @property
    @abstractmethod
    def initial_speed(self):
        pass

    @property
    @abstractmethod
    def score(self):
        pass

    @property
    @abstractmethod
    def bounce_height(self):
        pass

    @property
    @abstractmethod
    def child_ball_class(self):
        pass

    def split(self):
        if self.child_ball_class is None:
            return None

        left_position = (self.x - settings.ball_split_x, self.y)
        right_position = (self.x + settings.ball_split_x, self.y)

        left_child_ball = self.child_ball_class(left_position, Direction.LEFT)
        right_child_ball = self.child_ball_class(right_position, Direction.RIGHT)

        return left_child_ball, right_child_ball

    def update(self):
        self.x, self.y, self.x_speed, self.y_speed = physics.bounce(
            x=self.x,
            y=self.y,
            x_speed=self.x_speed,
            y_speed=self.y_speed,
            width=self.width,
            height=self.height,
            bounce_height=self.bounce_height,
            ground_y=settings.ground_y,
        )
        self.rect.center = (int(self.x), int(self.y))


class Ball_1(Ball):
    @property
    def dimensions(self):
        return settings.ball_1_dimensions

    @property
    def initial_speed(self):
        return settings.ball_1_initial_speed

    @property
    def score(self):
        return settings.ball_1_score

    @property
    def bounce_height(self):
        return settings.ball_1_bounce_height

    @property
    def child_ball_class(self):
        return None


class Ball_2(Ball):
    @property
    def dimensions(self):
        return settings.ball_2_dimensions

    @property
    def initial_speed(self):
        return settings.ball_2_initial_speed

    @property
    def score(self):
        return settings.ball_2_score

    @property
    def bounce_height(self):
        return settings.ball_2_bounce_height

    @property
    def child_ball_class(self):
        return Ball_1


class Ball_3(Ball):
    @property
    def dimensions(self):
        return settings.ball_3_dimensions

    @property
    def initial_speed(self):
        return settings.ball_3_initial_speed

    @property
    def score(self):
        return settings.ball_3_score

    @property
    def bounce_height(self):
        return settings.ball_3_bounce_height

    @property
    def child_ball_class(self):
        return Ball_2


class Ball_4(Ball):
    @property
    def dimensions(self):
        return settings.ball_4_dimensions

    @property
    def initial_speed(self):
        return settings.ball_4_initial_speed

    @property
    def score(self):
        return settings.ball_4_score

    @property
    def bounce_height(self):
        return settings.ball_4_bounce_height

    @property
    def child_ball_class(self):
        return Ball_3


class Ball_5(Ball):
    @property
    def dimensions(self):
        return settings.ball_5_dimensions

    @property
    def initial_speed(self):
        return settings.ball_5_initial_speed

    @property
    def score(self):
        return settings.ball_5_score

    @property
    def bounce_height(self):
        return settings.ball_5_bounce_height

    @property
    def child_ball_class(self):
        return Ball_4
