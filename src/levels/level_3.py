from src import settings
from src.entities.ball import Ball_2
from src.levels.level import Level

class Level_3(Level):
    @property
    def level_number(self):
        return 3

    @property
    def background_path(self):
        return settings.level_3_background_path

    def init_entities(self):
        ball_1 = Ball_2((100, settings.ball_y))
        ball_2 = Ball_2((300, settings.ball_y))
        ball_3 = Ball_2((500, settings.ball_y))
        ball_4 = Ball_2((700, settings.ball_y))
        self.ball_group.add(ball_1)
        self.ball_group.add(ball_2)
        self.ball_group.add(ball_3)
        self.ball_group.add(ball_4)
