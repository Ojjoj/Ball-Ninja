from src import settings
from src.entities.ball import Ball_3
from src.entities.stone import Stone_2
from src.utils.movement import Direction
from src.levels.level import Level

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
        stone_1 = Stone_2((0, settings.ball_y + 50))
        stone_2 = Stone_2((settings.screen_width - settings.stone_2_width, settings.ball_y + 50))

        self.ball_group.add(ball_1)
        self.ball_group.add(ball_2)
        self.stone_group.add(stone_1)
        self.stone_group.add(stone_2)

