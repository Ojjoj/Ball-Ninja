from src import settings
from src.entities.ball import Ball_3
from src.entities.ball import Ball_2
from src.entities.ball import Ball_1
from src.entities.stone import Stone_3
from src.levels.level import Level
from src.utils.movement import Direction

class Level_4(Level):
    @property
    def level_number(self):
        return 4

    @property
    def background_path(self):
        return settings.level_4_background_path

    def init_entities(self):
        ball_1 = Ball_1((100, settings.ball_y))
        ball_2 = Ball_2((300, settings.ball_y), Direction.LEFT)
        ball_3 = Ball_2((500, settings.ball_y))
        ball_4 = Ball_3((700, settings.ball_y), Direction.LEFT)

        stone_1 = Stone_3((settings.screen_width // 2 - settings.stone_3_width // 2, 200))

        self.ball_group.add(ball_1)
        self.ball_group.add(ball_2)
        self.ball_group.add(ball_3)
        self.ball_group.add(ball_4)

        self.stone_group.add(stone_1)
