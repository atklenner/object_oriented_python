import pygame
from pygame.locals import *
import sys
from pathlib import Path

# define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent

# initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets

# initialize variables

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # per frame actions

    # clear the window
    window.fill(BLACK)

    # draw all window elements

    # update the window
    pygame.display.update()

    # set frame rate
    clock.tick(FRAMES_PER_SECOND)
