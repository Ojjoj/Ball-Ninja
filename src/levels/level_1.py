from src import settings
from src.entities.ball import Ball_3
from src.levels.level import Level

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
