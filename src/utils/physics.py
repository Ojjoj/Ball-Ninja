import pygame
import math
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

    # Apply gravity first
    ball.y_speed += gravity

    # Calculate next position
    next_x = ball.x + ball.x_speed
    next_y = ball.y + ball.y_speed

    # Create future ball rect for collision detection
    future_ball_rect = pygame.Rect(0, 0, ball.rect.width, ball.rect.height)
    future_ball_rect.center = (int(next_x), int(next_y))

    # Check if collision will occur
    if not future_ball_rect.colliderect(stone.rect):
        return next_x, next_y, ball.x_speed, ball.y_speed

    # Calculate collision normal and response
    ball_center_x, ball_center_y = ball.rect.center
    stone_center_x, stone_center_y = stone.rect.center

    # Vector from stone center to ball center
    dx = ball_center_x - stone_center_x
    dy = ball_center_y - stone_center_y

    # Calculate overlaps
    ball_half_width = ball.rect.width / 2
    ball_half_height = ball.rect.height / 2
    stone_half_width = stone.rect.width / 2
    stone_half_height = stone.rect.height / 2

    overlap_x = ball_half_width + stone_half_width - abs(dx)
    overlap_y = ball_half_height + stone_half_height - abs(dy)

    # Determine collision side and resolve
    if overlap_x < overlap_y:
        # Horizontal collision (left/right sides)
        if dx > 0:
            # Ball is to the right of stone (hit left side of stone)
            next_x = stone.rect.right + ball_half_width
            ball.x_speed = abs(ball.x_speed) * elasticity
        else:
            # Ball is to the left of stone (hit right side of stone)
            next_x = stone.rect.left - ball_half_width
            ball.x_speed = -abs(ball.x_speed) * elasticity
    else:
        # Vertical collision (top/bottom sides)
        if dy > 0:
            # Ball is below stone (hit bottom of stone)
            next_y = stone.rect.bottom + ball_half_height
            ball.y_speed = abs(ball.y_speed) * elasticity
        else:
            # Ball is above stone (hit top of stone)
            next_y = stone.rect.top - ball_half_height
            # Realistic bounce: preserve energy but reverse direction
            ball.y_speed = -abs(ball.y_speed) * elasticity

    return next_x, next_y, ball.x_speed, ball.y_speed