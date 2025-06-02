import os

"""
- game settings
- score settings
- images paths
- animations images paths
- entities dimensions
- entities positions
- entities speeds
- balls scores
"""

# game settings
game_name = "Ball Ninja"

fps = 60
blur_radius = 2

screen_width = 800
screen_height = 600
screen_dimensions = (screen_width, screen_height)


# lives settings
initial_lives = 999
lives_x = 10
lives_y = 10
lives_position = (lives_x, lives_y)

# score settings
score_color = (255, 255, 255)
score_font = "Arial"
score_font_size = 30
score_x = screen_width - 30
score_y = 20
score_position = (score_x, score_y)

# images paths
images_path = os.path.join("assets", "images")

backgrounds_path = os.path.join(images_path, "backgrounds")
level_1_background_path = os.path.join(backgrounds_path, "baalbek.jpg")
level_2_background_path = os.path.join(backgrounds_path, "beirut.jpg")
level_3_background_path = os.path.join(backgrounds_path, "raouche.jpg")
level_4_background_path = os.path.join(backgrounds_path, "saida.jpg")
level_5_background_path = os.path.join(backgrounds_path, "tyre.jpg")
level_6_background_path = os.path.join(backgrounds_path, "hermel.jpg")

sprites_path = os.path.join(images_path, "sprites")
ball_path = os.path.join(sprites_path, "ball.png")
player_forward_path = os.path.join(sprites_path, "player_forward.png")
player_backward_path = os.path.join(sprites_path, "player_backward.png")
ground_path = os.path.join(sprites_path, "ground.png")
laser_path = os.path.join(sprites_path, "laser.png")
stone_path = os.path.join(sprites_path, "stone.png")

menus_path = os.path.join(images_path, "menus")
menus_backgrounds_path = os.path.join(menus_path, "backgrounds")
starting_image_path = os.path.join(menus_backgrounds_path, "starting_image.png")
winning_image_path = os.path.join(menus_backgrounds_path, "winning_image.png")
loosing_image_path = os.path.join(menus_backgrounds_path, "loosing_image.png")

# animations images paths
player_left_animation_path = os.path.join(sprites_path, "player_left_animation")
player_right_animation_path = os.path.join(sprites_path, "player_right_animation")
player_left_animation_images_paths = [
    os.path.join(player_left_animation_path, "player_left_1.png"),
    os.path.join(player_left_animation_path, "player_left_2.png"),
    os.path.join(player_left_animation_path, "player_left_3.png"),
    os.path.join(player_left_animation_path, "player_left_4.png"),
    os.path.join(player_left_animation_path, "player_left_5.png"),
    os.path.join(player_left_animation_path, "player_left_6.png"),
    os.path.join(player_left_animation_path, "player_left_7.png"),
    os.path.join(player_left_animation_path, "player_left_8.png"),
    os.path.join(player_left_animation_path, "player_left_9.png"),
    os.path.join(player_left_animation_path, "player_left_10.png"),
    os.path.join(player_left_animation_path, "player_left_11.png"),
    os.path.join(player_left_animation_path, "player_left_12.png"),
    os.path.join(player_left_animation_path, "player_left_13.png"),
    os.path.join(player_left_animation_path, "player_left_14.png"),
]
player_right_animation_images_paths = [
    os.path.join(player_right_animation_path, "player_right_1.png"),
    os.path.join(player_right_animation_path, "player_right_2.png"),
    os.path.join(player_right_animation_path, "player_right_3.png"),
    os.path.join(player_right_animation_path, "player_right_4.png"),
    os.path.join(player_right_animation_path, "player_right_5.png"),
    os.path.join(player_right_animation_path, "player_right_6.png"),
    os.path.join(player_right_animation_path, "player_right_7.png"),
    os.path.join(player_right_animation_path, "player_right_8.png"),
    os.path.join(player_right_animation_path, "player_right_9.png"),
    os.path.join(player_right_animation_path, "player_right_10.png"),
    os.path.join(player_right_animation_path, "player_right_11.png"),
    os.path.join(player_right_animation_path, "player_right_12.png"),
    os.path.join(player_right_animation_path, "player_right_13.png"),
    os.path.join(player_right_animation_path, "player_right_14.png"),
]

## entities dimensions
# player dimensions
player_width = 90
player_height = 193
player_dimensions = (player_width, player_height)

# ball dimensions
ball_1_height = 25
ball_1_width = 25
ball_1_dimensions = (ball_1_width, ball_1_height)
ball_2_height = 50
ball_2_width = 50
ball_2_dimensions = (ball_2_width, ball_2_height)
ball_3_height = 100
ball_3_width = 100
ball_3_dimensions = (ball_3_width, ball_3_height)
ball_4_height = 150
ball_4_width = 150
ball_4_dimensions = (ball_4_width, ball_4_height)
ball_5_height = 300
ball_5_width = 300
ball_5_dimensions = (ball_5_width, ball_5_height)

# laser dimensions
laser_width = 20
laser_height = 600
laser_dimensions = (laser_width, laser_height)

# stone dimensions
stone_1_height = 30
stone_1_width = 80
stone_1_dimensions = (stone_1_width, stone_1_height)
stone_2_height = 30
stone_2_width = 160
stone_2_dimensions = (stone_2_width, stone_2_height)
stone_3_height = 30
stone_3_width = 260
stone_3_dimensions = (stone_3_width, stone_3_height)

# entities positions
player_x = screen_width // 2
player_y = screen_height - 10
player_position = (player_x, player_y)

ball_x = screen_width // 2
ball_y = 100
ball_position = (ball_x, ball_y)

ball_split_x = 10

ground_y = screen_height - 35

# entities speeds
gravity = 0.12
elasticity = 1.0

ball_1_initial_speed_x = 2
ball_1_initial_speed_y = -2
ball_1_initial_speed = (ball_1_initial_speed_x, ball_1_initial_speed_y)
ball_2_initial_speed_x = 2
ball_2_initial_speed_y = -2
ball_2_initial_speed = (ball_1_initial_speed_x, ball_1_initial_speed_y)
ball_3_initial_speed_x = 2
ball_3_initial_speed_y = -2
ball_3_initial_speed = (ball_1_initial_speed_x, ball_1_initial_speed_y)
ball_4_initial_speed_x = 2
ball_4_initial_speed_y = -2
ball_4_initial_speed = (ball_1_initial_speed_x, ball_1_initial_speed_y)
ball_5_initial_speed_x = 2
ball_5_initial_speed_y = -2
ball_5_initial_speed = (ball_1_initial_speed_x, ball_1_initial_speed_y)

ball_1_bounce_height = 200
ball_2_bounce_height = 250
ball_3_bounce_height = 300
ball_4_bounce_height = 450
ball_5_bounce_height = 500

animation_speed = 0.4
player_speed = 6
player_die_speed_x = 0
player_die_speed_y = 6
player_die_speed = (player_die_speed_x, player_die_speed_y)

laser_speed = 10

# balls scores
ball_1_score = 10
ball_2_score = 8
ball_3_score = 6
ball_4_score = 4
ball_5_score = 2
