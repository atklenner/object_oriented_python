import pygame
from pygame.locals import *
import sys
from pathlib import Path
from Ball import *
from SimpleButton import *
from SimpleText import *

# define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = str(Path(__file__).resolve().parent)
N_BALLS = 30

# initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets

# initialize variables
restart_button_up = BASE_PATH + "/images/restart_button_up.png"
restart_button_down = BASE_PATH + "/images/restart_button_down.png"
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
frame_count_label = SimpleText(
    window, (60, 20), "Program has run this many loops: ", WHITE)
frame_count_display = SimpleText(window, (500, 20), "", WHITE)
restart_button = SimpleButton(
    window, (280, 60), restart_button_up, restart_button_down)
frame_counter = 0

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if restart_button.handle_event(event):
            frame_counter = 0

    # per frame actions
    ball.update()
    frame_counter += 1
    frame_count_display.set_value(str(frame_counter))

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    ball.draw()
    frame_count_label.draw()
    frame_count_display.draw()
    restart_button.draw()

    # update the window
    pygame.display.update()

    # set frame rate
    clock.tick(FRAMES_PER_SECOND)
