import pygame
import sys

from src import settings
from src.levels.levels import load_levels


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.screen_dimensions)
        pygame.display.set_caption(settings.game_name)
        self.clock = pygame.time.Clock()

        self.levels = iter(load_levels())
        self.current_level = next(self.levels, None)

    def run(self):
        while self.current_level:
            self.play_level(self.current_level)
            self.current_level = next(self.levels, None)
        self.exit()

    def play_level(self, level):
        level.start(self.screen)
        while level.running:
            self.handle_events(level)
            level.update()
            level.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(settings.fps)

    def handle_events(self, level):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            level.handle_event(event)

    def exit(self):
        pygame.quit()
        sys.exit()
