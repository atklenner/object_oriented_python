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
N_PIXELS_TO_MOVE = 3

# initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets
path_to_ball = str(BASE_PATH) + "/images/ball.png"
ball_image = pygame.image.load(path_to_ball)

# another way to do it
# ball_image = pygame.image.load(
#     Path("object_oriented_python/chapter_5/images/ball.png"))

# initialize variables
ball_rect = ball_image.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ball_rect.width
MAX_HEIGHT = WINDOW_HEIGHT - ball_rect.height
ball_rect.left = random.randrange(MAX_WIDTH)
ball_rect.top = random.randrange(MAX_HEIGHT)
x_speed = N_PIXELS_TO_MOVE
y_speed = N_PIXELS_TO_MOVE

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # per frame actions
    if ball_rect.left < 0 or ball_rect.right >= WINDOW_WIDTH:
        x_speed = -x_speed

    if ball_rect.top < 0 or ball_rect.bottom >= WINDOW_HEIGHT:
        y_speed = -y_speed

    ball_rect.left += x_speed
    ball_rect.top += y_speed

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    window.blit(ball_image, ball_rect)

    # update the window
    pygame.display.update()

    # set frame rate
    clock.tick(FRAMES_PER_SECOND)
