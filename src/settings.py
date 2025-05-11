import os

# game settings
game_name = "Ball Ninja"

screen_width = 800
screen_height = 600
screen_dimensions = (screen_width, screen_height)

# image paths
images_path = os.path.join("assets", "images")

level_1_background_path = os.path.join(images_path, "baalbek.jpg")
level_2_background_path = os.path.join(images_path, "beirut.jpg")
level_3_background_path = os.path.join(images_path, "raouche.jpg")
level_4_background_path = os.path.join(images_path, "saida.jpg")
level_5_background_path = os.path.join(images_path, "tyre.jpg")
level_6_background_path = os.path.join(images_path, "hermel.jpg")

ball_path = os.path.join(images_path, "ball.png")
player_path = os.path.join(images_path, "player.png")

# entities dimensions
player_width = 128
player_height = 128
player_dimensions = (player_width, player_height)

ball_1_height = 128
ball_1_width = 128
ball_1_dimensions = (ball_1_width, ball_1_height)
# TODO: more types

# entities sizes
player_position = screen_width // 2, screen_height - 10

ball_position = screen_width // 2

# ball scores
ball_1_score = 10
ball_2_score = 8
ball_3_score = 6
ball_4_score = 4
ball_5_score = 2
