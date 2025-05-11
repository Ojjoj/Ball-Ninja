from src import settings


class Level:
    def __init__(self, level_number, background):
        self.level_number = level_number
        self.background = background

    def title(self):
        return f"{settings.game_name}: {self.level_number}"


# level 1
level_1 = Level(
    level_number=1,
    background=settings.level_1_background_path
)
