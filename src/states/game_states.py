import pygame
from src import settings


class GameState:
    def __init__(self, game, message, color=(255, 255, 255), background_path=None):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.SysFont(settings.score_font, 60)
        self.message = message
        self.color = color
        self.background = self.load_background(background_path)

    def load_background(self, path):
        if path:
            image = pygame.image.load(path).convert()
            return pygame.transform.scale(image, settings.screen_dimensions)
        else:
            return pygame.Surface(settings.screen_dimensions).convert()

    def run(self):
        text = self.font.render(self.message, True, self.color)
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        while True:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(text, rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return

class StartState(GameState):
    def __init__(self, game):
        super().__init__(
            game,
            message="Press SPACE to Start",
            background_path=settings.starting_image_path
        )

class WinState(GameState):
    def __init__(self, game):
        super().__init__(
            game,
            message="Press SPACE for next level",
            background_path=settings.winning_image_path
        )


class GameOverState(GameState):
    def __init__(self, game):
        super().__init__(
            game,
            message="Press SPACE to restart",
            background_path=settings.loosing_image_path
        )
