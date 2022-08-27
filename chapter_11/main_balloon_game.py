import pygame
from pygame.locals import *
import sys
import pygwidgets
from BalloonManager import *
from constants import N_BALLOONS

# define constants
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets
score_display = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25), "Score: 0", textColor=BLACK, backgroundColor=None, width=140, fontSize=24)
status_display = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25), "", textColor=BLACK, width=300, fontSize=24)
start_button = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), "Start")

# initialize variables
balloon_manager = BalloonManager(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            balloon_manager.handle_event(event)
            score = balloon_manager.get_score()
            score_display.setValue("Score: " + str(score))
        elif start_button.handleEvent(event):
            balloon_manager.start()
            score_display.setValue("Score: 0")
            playing = True
            start_button.disable()

    # per frame actions
    if playing:
        balloon_manager.update()
        number_popped = balloon_manager.get_count_popped()
        number_missed = balloon_manager.get_count_missed()
        status_display.setValue("Popped: " + str(number_popped) + "   Missed: " + str(number_missed) + "   Out of: " + str(N_BALLOONS))

        if (number_missed + number_popped) == N_BALLOONS:
            playing = False
            start_button.enable()

    # clear the window
    window.fill(BACKGROUND_COLOR)

    # draw all window elements
    if playing:
        balloon_manager.draw()

    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    score_display.draw()
    status_display.draw()
    start_button.draw()

    # update the window
    pygame.display.update()

    # set frame rate
    clock.tick(FRAMES_PER_SECOND)
