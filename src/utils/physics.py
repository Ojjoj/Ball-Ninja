import pygame
from src import settings

def velocity(gravity, height):
    return (2 * gravity * height) ** 0.5

def bounce(x, y, x_speed, y_speed, width, height, bounce_height, ground_y):
    gravity = settings.gravity
    elasticity = settings.elasticity
    screen_width = settings.screen_width

    floor_y = ground_y - height / 2
    ceiling_y = height / 2
    min_x = width / 2
    max_x = screen_width - width / 2

    y_speed += gravity

    x += x_speed
    y += y_speed

    # Bounce off floor
    if y >= floor_y and y_speed > 0:
        y = floor_y
        y_speed = -velocity(gravity, bounce_height)

    # Bounce off ceiling
    elif y <= ceiling_y and y_speed < 0:
        y = ceiling_y
        y_speed *= -1

    # Bounce off left wall
    if x <= min_x and x_speed < 0:
        x = min_x
        x_speed *= -elasticity

    # Bounce off right wall
    elif x >= max_x and x_speed > 0:
        x = max_x
        x_speed *= -elasticity

    return x, y, x_speed, y_speed

def collide_with_stone(ball, stone):
    gravity = settings.gravity
    elasticity = settings.elasticity

    ball.y_speed += gravity

    next_x = ball.x + ball.x_speed
    next_y = ball.y + ball.y_speed

    future_rect = ball.rect.copy()
    future_rect.center = (int(next_x), int(next_y))

    # Collision mask
    if pygame.sprite.collide_mask(ball, stone):
        dx = ball.rect.centerx - stone.rect.centerx
        dy = ball.rect.centery - stone.rect.centery

        abs_dx = abs(dx)
        abs_dy = abs(dy)

        overlap_x = (ball.rect.width + stone.rect.width) / 4 - abs_dx
        overlap_y = (ball.rect.height + stone.rect.height) / 4 - abs_dy

        if overlap_y < overlap_x:
            # Vertical bounce
            if dy > 0 and ball.y_speed < 0:
                # Hit from below
                next_y = stone.rect.bottom + ball.rect.height / 2
                ball.y_speed *= -1
            elif dy < 0 and ball.y_speed > 0:
                # Hit from top
                next_y = stone.rect.top - ball.rect.height / 2
                ball.y_speed = -velocity(gravity, ball.bounce_height / 2)
        else:
            # Horizontal bounce
            if dx > 0 and ball.x_speed < 0:
                next_x = stone.rect.right + ball.rect.width / 2
                ball.x_speed *= -elasticity
            elif dx < 0 and ball.x_speed > 0:
                next_x = stone.rect.left - ball.rect.width / 2
                ball.x_speed *= -elasticity

    return next_x, next_y, ball.x_speed, ball.y_speed
