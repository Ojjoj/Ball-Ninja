import pygame

from src import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, position=settings.player_position):
        super().__init__()

        player_image_path = settings.player_backward_path
        player_image = pygame.image.load(player_image_path).convert_alpha()

        self.idle_image = pygame.transform.scale(player_image, settings.player_dimensions)

        self.direction = "idle"
        self.frame_index = 0

        self.image = self.idle_image
        self.rect = self.image.get_rect(midbottom=position)

        self.left_animation = self.load_animation("left")
        self.right_animation = self.load_animation("right")

    def load_animation(self, animation_type):
        if animation_type == "right":
            animation_images_paths = settings.player_right_animation_images_paths
        else:
            animation_images_paths = settings.player_left_animation_images_paths

        images = []
        for image_path in animation_images_paths:
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, settings.player_dimensions)
            images.append(image)
        return images

    def update(self, keys):
        # Handle input
        if keys[pygame.K_LEFT]:
            self.direction = "left"
            self.rect.x -= settings.player_speed
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.rect.x += settings.player_speed
        else:
            self.direction = "idle"
            self.frame_index = 0

        # Clamp to screen
        self.rect.clamp_ip(pygame.Rect(0, 0, settings.screen_width, settings.screen_height))

        # Update animation
        if self.direction == "left":
            self.frame_index += settings.animation_speed
            if self.frame_index >= len(self.left_animation):
                self.frame_index = 0
            self.image = self.left_animation[int(self.frame_index)]
        elif self.direction == "right":
            self.frame_index += settings.animation_speed
            if self.frame_index >= len(self.right_animation):
                self.frame_index = 0
            self.image = self.right_animation[int(self.frame_index)]
        else:
            self.image = self.idle_image
