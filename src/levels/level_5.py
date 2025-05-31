from src import settings
from src.entities.ball import Ball_4
from src.levels.level import Level

class Level_5(Level):
    @property
    def level_number(self):
        return 5

    @property
    def background_path(self):
        return settings.level_5_background_path

    def init_entities(self):
        ball_1 = Ball_4(settings.ball_position)

        self.ball_group.add(ball_1)
