import pygame

from abc import ABC, abstractmethod
import math

from src import settings


class Ball(ABC, pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        ball_path = settings.ball_path
        original_image = pygame.image.load(ball_path).convert_alpha()
        self.width, self.height = self.get_dimensions()
        self.image = pygame.transform.scale(original_image, (self.width, self.height))
        self.position = self.get_position()
        self.rect = self.image.get_rect(center=self.position)
        self.x, self.y = float(self.rect.centerx), float(self.rect.centery)
        self.x_speed, self.y_speed = self.get_initial_speed()
        self.initial_y_speed = abs(self.y_speed)
        self.score = self.get_score()
        self.bounce_height = self.get_bounce_height()
        self.child_balls = self.get_child_ball_type()

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_dimensions(self):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def get_initial_speed(self):
        pass

    @abstractmethod
    def get_score(self):
        pass

    @abstractmethod
    def get_bounce_height(self):
        pass

    @abstractmethod
    def get_child_ball_type(self):
        pass

    def split(self):
        child_type = self.get_child_ball_type()
        if not child_type:
            return None

        left_ball = eval(child_type)
        left_ball.position = self.position + self.width // 2

        right_ball = eval(child_type)
        right_ball.position = self.position - self.width // 2

        return left_ball, right_ball

    def update(self):
        # Apply gravity
        self.y_speed += settings.gravity

        # Move
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.center = (int(self.x), int(self.y))

        # Bounce off floor - with consistent bounce height
        floor_y = settings.ground_y - self.height / 2
        if self.y >= floor_y and self.y_speed > 0:
            self.y = floor_y
            # Calculate the speed needed to reach the desired bounce height
            self.y_speed = -math.sqrt(2 * settings.gravity * self.bounce_height)

        # Bounce off ceiling
        ceil_y = self.height / 2
        if self.y <= ceil_y and self.y_speed < 0:
            self.y = ceil_y
            self.y_speed *= -1

        # Bounce off left wall
        left_x = self.width / 2
        if self.x <= left_x and self.x_speed < 0:
            self.x = left_x
            self.x_speed *= -settings.elasticity

        # Bounce off right wall
        right_x = settings.screen_width - self.width / 2
        if self.x >= right_x and self.x_speed > 0:
            self.x = right_x
            self.x_speed *= -settings.elasticity


class Ball_1(Ball):
    def __repr__(self):
        return "Ball_1"

    def get_dimensions(self):
        return settings.ball_1_dimensions

    def get_position(self):
        return settings.ball_1_position

    def get_initial_speed(self):
        return settings.ball_1_initial_speed

    def get_score(self):
        return settings.ball_1_score

    def get_bounce_height(self):
        return settings.ball_1_bounce_height

    def get_child_ball_type(self):
        return settings.ball_1_child


class Ball_2(Ball):
    def __repr__(self):
        return "Ball_2"

    def get_dimensions(self):
        return settings.ball_2_dimensions

    def get_position(self):
        return settings.ball_2_position

    def get_initial_speed(self):
        return settings.ball_2_initial_speed

    def get_score(self):
        return settings.ball_2_score

    def get_bounce_height(self):
        return settings.ball_2_bounce_height

    def get_child_ball_type(self):
        return settings.ball_2_child


class Ball_3(Ball):
    def __repr__(self):
        return "Ball_3"

    def get_dimensions(self):
        return settings.ball_3_dimensions

    def get_position(self):
        return settings.ball_3_position

    def get_initial_speed(self):
        return settings.ball_3_initial_speed

    def get_score(self):
        return settings.ball_3_score

    def get_bounce_height(self):
        return settings.ball_3_bounce_height

    def get_child_ball_type(self):
        return settings.ball_3_child


class Ball_4(Ball):
    def __repr__(self):
        return "Ball_4"

    def get_dimensions(self):
        return settings.ball_4_dimensions

    def get_position(self):
        return settings.ball_4_position

    def get_initial_speed(self):
        return settings.ball_4_initial_speed

    def get_score(self):
        return settings.ball_4_score

    def get_bounce_height(self):
        return settings.ball_4_bounce_height

    def get_child_ball_type(self):
        return settings.ball_4_child


class Ball_5(Ball):
    def __repr__(self):
        return "Ball_5"

    def get_dimensions(self):
        return settings.ball_5_dimensions

    def get_position(self):
        return settings.ball_5_position

    def get_initial_speed(self):
        return settings.ball_5_initial_speed

    def get_score(self):
        return settings.ball_5_score

    def get_bounce_height(self):
        return settings.ball_5_bounce_height

    def get_child_ball_type(self):
        return settings.ball_5_child
