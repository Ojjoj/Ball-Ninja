import pygame
import sys

from src import settings
from src.levels.levels import Level


class Game:
    def __init__(self):
        pygame.init()
        Level.game = self
        self.screen = pygame.display.set_mode(settings.screen_dimensions)
        pygame.display.set_caption(settings.game_name)
        self.clock = pygame.time.Clock()
        self.score = 0
        self.total_lives = settings.initial_lives
        self.font = pygame.font.SysFont(settings.score_font, settings.score_font_size)
        self.levels = iter(Level.load_levels())
        self.current_level = next(self.levels, None)

    def run(self):
        while self.current_level:
            self.play_level(self.current_level)
            self.current_level = next(self.levels, None)
        self.exit()

    def draw_ui(self):
        self.draw_score()
        self.draw_lives()

    def draw_score(self):
        text = self.font.render(f"Score: {self.score}", True, settings.score_color)
        text_rect = text.get_rect(topright=settings.score_position)
        self.screen.blit(text, text_rect)

    def draw_lives(self):
        lives_text = self.font.render(f"Lives: {self.total_lives}", True, settings.score_color)
        lives_rect = lives_text.get_rect(topleft=settings.lives_position)
        self.screen.blit(lives_text, lives_rect)

    def play_level(self, level):
        level.start()
        while level.running:
            self.handle_events(level)
            level.update()
            level.draw(self.screen)
            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(settings.fps)
        else:
            if self.total_lives > 0:
                self.play_level(type(level)())
            else:
                self.exit()


    def handle_events(self, level):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            level.handle_event(event)

    def exit(self):
        pygame.quit()
        sys.exit()
