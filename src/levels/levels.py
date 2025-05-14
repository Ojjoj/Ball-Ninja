from src.entities.player import Player
from src.entities.laser import Laser
from src.entities.ball import *
from src.utils import graphics


def load_levels():
    level_1 = Level_1()
    level_2 = Level_2()
    level_3 = Level_3()
    return [level_1, level_2, level_3]

class Level(ABC):
    def __init__(self):
        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle(self.player)

        self.laser_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()

        self.running = True

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

    def start(self, screen):
        self.running = True

    def update(self):
        keys = pygame.key.get_pressed()
        self.player_group.update(keys)
        self.ball_group.update()
        self.laser_group.update()
        self.handle_collisions()

        if len(self.ball_group) == 0:
            self.running = False

    def handle_collisions(self):
        for laser in self.laser_group:
            ball_collided = pygame.sprite.spritecollideany(laser, self.ball_group)
            if ball_collided:
                laser.kill()
                self.ball_group.remove(ball_collided)
                children_balls = ball_collided.split()
                if children_balls is not None:
                    self.ball_group.add(*children_balls)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.ground, (0, settings.screen_height - 80))
        self.laser_group.draw(screen)
        self.ball_group.draw(screen)
        self.player_group.draw(screen)

# Level_1
class Level_1(Level):
    @property
    def level_number(self):
        return 1

    @property
    def background_path(self):
        return settings.level_1_background_path

    def init_entities(self):
        self.ball_group.add(Ball_3(settings.ball_position))

# Level_2
class Level_2(Level):
    @property
    def level_number(self):
        return 1

    @property
    def background_path(self):
        return settings.level_2_background_path

    def init_entities(self):
        self.ball_group.add(Ball_4(settings.ball_position))

# Level_3
class Level_3(Level):
    @property
    def level_number(self):
        return 1

    @property
    def background_path(self):
        return settings.level_3_background_path

    def init_entities(self):
        self.ball_group.add(Ball_5(settings.ball_position))

