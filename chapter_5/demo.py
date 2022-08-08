import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random

# define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets
path_to_ball = str(BASE_PATH) + "/images/ball.png"
# path_to_target = str(BASE_PATH) + "/images/target.jpg"
ball_image = pygame.image.load(path_to_ball)
# target_image = pygame.image.load(path_to_target)

# another way to do it
# ball_image = pygame.image.load(
#     Path("object_oriented_python/chapter_5/images/ball.png"))

# initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_TO_MOVE
y_speed = N_PIXELS_TO_MOVE
# ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
# target_rect = pygame.Rect(
# TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # key_pressed_tuple = pygame.key.get_pressed()

    # if key_pressed_tuple[pygame.K_LEFT]:
    #     ball_x -= N_PIXELS_TO_MOVE
    # if key_pressed_tuple[pygame.K_RIGHT]:
    #     ball_x += N_PIXELS_TO_MOVE
    # if key_pressed_tuple[pygame.K_UP]:
    #     ball_y -= N_PIXELS_TO_MOVE
    # if key_pressed_tuple[pygame.K_DOWN]:
    #     ball_y += N_PIXELS_TO_MOVE

    if (ball_x < 0) or ball_x >= MAX_WIDTH:
        x_speed = -x_speed

    if ball_y < 0 or ball_y >= MAX_HEIGHT:
        y_speed = -y_speed

    ball_x += x_speed
    ball_y += y_speed

    # per frame actions
    # ball_rect = pygame.Rect(
    # ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # if ball_rect.colliderect(target_rect):
    # print("Ball is touching target")

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    # window.blit(target_image, (TARGET_X, TARGET_Y))
    window.blit(ball_image, (ball_x, ball_y))

    # update the window
    pygame.display.update()

    # set frame rate
    clock.tick(FRAMES_PER_SECOND)
