import pygame
import sys

from src import settings


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(settings.screen_dimensions)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(settings.game_name)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(background_image, (0, 0))
            self.screen.blit(ground_image, (0, HEIGHT - 80))
            self.screen.blit(player)
            ball_group.draw(screen)
            pygame.display.flip()

    def exit(self):
        pygame.quit()
        sys.exit()
