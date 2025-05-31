from src import settings
from src.entities.ball import Ball_4
from src.entities.stone import Stone_2
from src.utils.movement import Direction
from src.levels.level import Level

class Level_6(Level):
    @property
    def level_number(self):
        return 6

    @property
    def background_path(self):
        return settings.level_6_background_path

    def init_entities(self):
        ball_1 = Ball_4((settings.ball_4_width, settings.ball_y))
        ball_2 = Ball_4((settings.screen_width - settings.ball_4_width, settings.ball_y), Direction.LEFT)
        stone_1 = Stone_2((0, settings.ball_y + 85))
        stone_2 = Stone_2((settings.screen_width - settings.stone_2_width, settings.ball_y + 85))

        self.ball_group.add(ball_1)
        self.ball_group.add(ball_2)
        self.stone_group.add(stone_1)
        self.stone_group.add(stone_2)

