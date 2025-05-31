from abc import ABC, abstractmethod
import pygame

from src.entities.player import Player
from src.entities.laser import Laser
from src.entities.ball import *
from src.entities.stone import *
from src import settings
from src.utils import graphics, physics


class Level(ABC):
    game = None

    def __init__(self):
        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle(self.player)

        self.laser_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.stone_group = pygame.sprite.Group()

        self.running = True
        self.collision_score = 0
        self.lives_used = 0

        self.background = self.get_background_image()
        self.ground = self.get_ground()
        self.init_entities()

    @property
    @abstractmethod
    def level_number(self):
        pass

    @property
    @abstractmethod
    def background_path(self):
        pass

    @abstractmethod
    def init_entities(self):
        pass

    def get_background_image(self):
        image = pygame.image.load(self.background_path).convert()
        image = pygame.transform.scale(image, settings.screen_dimensions)
        return graphics.gaussian_blur(image, settings.blur_radius)

    def get_ground(self):
        image = pygame.image.load(settings.ground_path).convert()
        return pygame.transform.scale(image, (settings.screen_width, 80))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(self.laser_group) == 0:
                x = self.player.rect.centerx
                laser = Laser(x)
                self.laser_group.add(laser)

    def start(self):
        self.running = True

    def update(self):
        if self.player.is_dead:
            self.player.die_animation()
            if self.player.has_fallen_off_screen():
                self.running = False
            return

        keys = pygame.key.get_pressed()
        self.player_group.update(keys)
        self.ball_group.update()
        self.laser_group.update()

        self.handle_collisions()

        if len(self.ball_group) == 0:
            self.running = False

    def handle_collisions(self):
        self.laser_ball_collision()
        self.player_ball_collision()
        self.ball_stone_collision()
        self.laser_stone_collision()

    def laser_ball_collision(self):
        self.collision_score = 0
        for laser in self.laser_group:
            ball_collided = pygame.sprite.spritecollideany(laser, self.ball_group)
            if ball_collided:
                laser.kill()
                self.ball_group.remove(ball_collided)
                Level.game.score += ball_collided.score
                children_balls = ball_collided.split()
                if children_balls is not None:
                    self.ball_group.add(*children_balls)

    def player_ball_collision(self):
        player_collided = pygame.sprite.spritecollideany(self.player, self.ball_group, pygame.sprite.collide_mask)
        if player_collided:
            Level.game.total_lives -= 1
            self.player.is_dead = True

    def ball_stone_collision(self):
        for ball in self.ball_group:
            collided_stone = pygame.sprite.spritecollideany(ball, self.stone_group, pygame.sprite.collide_mask)
            if not collided_stone:
                continue
            ball.x, ball.y, ball.x_speed, ball.y_speed = physics.collide_with_stone(
                ball, collided_stone
            )
            ball.rect.center = (int(ball.x), int(ball.y))

    def laser_stone_collision(self):
        for laser in self.laser_group:
            if pygame.sprite.spritecollideany(laser, self.stone_group, pygame.sprite.collide_mask):
                laser.kill()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.ground, (0, settings.screen_height - 80))
        self.stone_group.draw(screen)
        self.laser_group.draw(screen)
        self.ball_group.draw(screen)
        self.player_group.draw(screen)

    def restart_level(self):
        self.__init__()

    @staticmethod
    def load_levels():
        level_1 = Level_1()
        level_2 = Level_2()
        level_3 = Level_3()
        return [level_1, level_2, level_3]


# Level_1
class Level_1(Level):
    @property
    def level_number(self):
        return 1

    @property
    def background_path(self):
        return settings.level_1_background_path

    def init_entities(self):
        ball = Ball_3(settings.ball_position)
        self.ball_group.add(ball)
        self.stone_group.add(Stone_1((300, 300)))


# Level_2
class Level_2(Level):
    @property
    def level_number(self):
        return 2

    @property
    def background_path(self):
        return settings.level_2_background_path

    def init_entities(self):
        ball_1 = Ball_3((settings.ball_3_width, settings.ball_y))
        ball_2 = Ball_3((settings.screen_width - settings.ball_3_width, settings.ball_y), Direction.LEFT)
        self.ball_group.add(ball_1)
        self.ball_group.add(ball_2)
        self.stone_group.add(Stone_2((400, 180)))


# Level_3
class Level_3(Level):
    @property
    def level_number(self):
        return 3

    @property
    def background_path(self):
        return settings.level_3_background_path

    def init_entities(self):
        self.ball_group.add(Ball_5(settings.ball_position))
        self.stone_group.add(Stone_3((500, 150)))
