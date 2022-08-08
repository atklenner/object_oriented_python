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
button_a_up_path = BASE_PATH + "/images/button_a_up.png"
button_a_down_path = BASE_PATH + "/images/button_a_down.png"
button_b_up_path = BASE_PATH + "/images/button_b_up.png"
button_b_down_path = BASE_PATH + "/images/button_b_down.png"
button_c_up_path = BASE_PATH + "/images/button_c_up.png"
button_c_down_path = BASE_PATH + "/images/button_c_down.png"
button_a = SimpleButton(window, (25, 30), button_a_up_path, button_a_down_path)
button_b = SimpleButton(window, (150, 30), button_b_up_path, button_b_up_path)
button_c = SimpleButton(
    window, (275, 30), button_c_up_path, button_c_down_path)

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if button_a.handle_event(event):
            print("button a clicked")
        elif button_b.handle_event(event):
            print("button b clicked")
        elif button_c.handle_event(event):
            print("button c clicked")

    # per frame actions

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    button_a.draw()
    button_b.draw()
    button_c.draw()

    # update the window
    pygame.display.update()

    # set frame rate
    clock.tick(FRAMES_PER_SECOND)
