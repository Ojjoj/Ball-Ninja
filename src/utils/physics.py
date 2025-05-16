import math
from src import settings


def velocity(gravity, bounce_height):
    return math.sqrt(2 * gravity * bounce_height)


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

