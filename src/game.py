import pygame
import sys

from src import settings
from src.levels.level import Level
from src.states.game_states import *
from src.levels import level_loader


class Game:
    def __init__(self):
        pygame.init()
        Level.game = self
        pygame.display.set_caption(settings.game_name)

        self.screen = pygame.display.set_mode(settings.screen_dimensions)
        self.clock = pygame.time.Clock()
        self.score = 0
        self.total_lives = settings.initial_lives
        self.levels = iter(level_loader.load_levels())
        self.current_level = next(self.levels, None)

    def run(self):
        StartState(self).run()
        while True:
            if self.current_level:
                self.play_level(self.current_level)
                if self.total_lives > 0:
                    WinState(self).run()
                    self.current_level = next(self.levels, None)
                else:
                    GameOverState(self).run()
                    self.reset_game()
            else:
                GameOverState(self).run()
                self.reset_game()

    def reset_game(self):
        self.score = 0
        self.total_lives = settings.initial_lives
        self.levels = iter(Level.load_levels())
        self.current_level = next(self.levels, None)

    def draw_ui(self):
        font = pygame.font.SysFont(settings.score_font, settings.score_font_size)
        self.draw_score(font)
        self.draw_lives(font)

    def draw_score(self, font):
        score_text = font.render(f"Score: {self.score}", True, settings.score_color)
        score_rect = score_text.get_rect(topright=settings.score_position)
        self.screen.blit(score_text, score_rect)

    def draw_lives(self, font):
        lives_text = font.render(f"Lives: {self.total_lives}", True, settings.score_color)
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
        if level.player.is_dead:
            if self.total_lives > 0:
                self.current_level = type(level)()
                self.play_level(self.current_level)

    def handle_events(self, level):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            level.handle_event(event)

    def exit(self):
        pygame.quit()
        sys.exit()
