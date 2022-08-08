from tkinter import Button
import pygame
from pygame.locals import *
import sys
from pathlib import Path
from SimpleButton import *

# define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = str(Path(__file__).resolve().parent)

# initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets

# initialize variables
button_up_path = BASE_PATH + "/images/button_up.png"
button_down_path = BASE_PATH + "/images/button_down.png"
button = SimpleButton(window, (150, 30), button_up_path, button_down_path)

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if button.handle_event(event):
            print("button clicked")

    # per frame actions

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    button.draw()

    # update the window
    pygame.display.update()

    # set frame rate
    clock.tick(FRAMES_PER_SECOND)
