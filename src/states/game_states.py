import pygame
import time
from src import settings

class Menu:
    def __init__(self, game, options, title=None, parent=None):
        self.game = game
        self.screen = game.screen
        self.options = options
        self.selected_index = 0
        self.font = pygame.font.SysFont(settings.score_font, 50, bold=False)
        self.highlight_font = pygame.font.SysFont(settings.score_font, 50, bold=True)
        self.background = self.load_background(settings.starting_image_path)
        self.title = title
        self.parent = parent

    def load_background(self, path):
        image = pygame.image.load(path).convert()
        return pygame.transform.scale(image, settings.screen_dimensions)

    def fade_transition(self):
        fade = pygame.Surface(settings.screen_dimensions)
        fade.fill((0, 0, 0))
        for alpha in range(0, 300, 15):
            fade.set_alpha(alpha)
            self.screen.blit(self.background, (0, 0))
            pygame.display.update()
            pygame.time.delay(30)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if self.title:
            title_font = pygame.font.SysFont(settings.score_font, 60, bold=True)
            title_surface = title_font.render(self.title, True, (255, 255, 255))
            title_rect = title_surface.get_rect(center=(self.screen.get_width() // 2, 100))
            self.screen.blit(title_surface, title_rect)

        for i, (text, _) in enumerate(self.options):
            is_selected = i == self.selected_index
            font = self.highlight_font if is_selected else self.font
            color = (255, 255, 0) if is_selected else (255, 255, 255)
            label_surface = font.render(text, True, color)
            label_rect = label_surface.get_rect(center=(self.screen.get_width() // 2, 200 + i * 60))
            self.screen.blit(label_surface, label_rect)

    def run(self):
        self.fade_transition()
        while True:
            self.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_SPACE:
                        _, action = self.options[self.selected_index]
                        if isinstance(action, Menu):
                            action.run()
                        elif callable(action):
                            action()
                        return  # Exit menu after selection

def create_main_menu(game):
    def about_us():
        show_text_screen(game, "Developed by Karam\nSpecial Thanks to Curl", "About Us")

    def settings_menu():
        toggles = [("Sound", True), ("Music", True)]

        def toggle(index):
            toggles[index] = (toggles[index][0], not toggles[index][1])

        def build_options():
            return [(f"{name}: {'On' if state else 'Off'}", lambda idx=i: toggle(idx)) for i, (name, state) in enumerate(toggles)] + [("Back", lambda: None)]

        settings_menu = Menu(game, build_options(), title="Settings")
        settings_menu.run()

    single_menu = Menu(game, [
        ("New Game", lambda: game.start_new_game("single")),
        ("Load Game", lambda: game.load_game("single")),
        ("Back", lambda: None)
    ], title="Single Play")

    multi_menu = Menu(game, [
        ("New Game", lambda: game.start_new_game("multi")),
        ("Load Game", lambda: game.load_game("multi")),
        ("Back", lambda: None)
    ], title="Multi Play")

    play_menu = Menu(game, [
        ("Single Play", single_menu),
        ("Multi Play", multi_menu),
        ("Back", lambda: None)
    ], title="Play")

    main_menu = Menu(game, [
        ("Play", play_menu),
        ("Settings", settings_menu),
        ("About Us", about_us),
        ("Exit", game.exit)
    ], title="Main Menu")

    return main_menu

def show_text_screen(game, text, title):
    screen = game.screen
    background = pygame.image.load(settings.starting_image_path).convert()
    background = pygame.transform.scale(background, settings.screen_dimensions)

    font = pygame.font.SysFont(settings.score_font, 40)
    lines = text.split("\n")
    texts = [font.render(line, True, (255, 255, 255)) for line in lines]
    running = True

    while running:
        screen.blit(background, (0, 0))
        title_font = pygame.font.SysFont(settings.score_font, 50, bold=True)
        title_surface = title_font.render(title, True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(screen.get_width() // 2, 80))
        screen.blit(title_surface, title_rect)

        for i, surf in enumerate(texts):
            rect = surf.get_rect(center=(screen.get_width() // 2, 200 + i * 50))
            screen.blit(surf, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
