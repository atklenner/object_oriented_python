from audioop import reverse
import pygame
import random
from pygame.locals import *
import pygwidgets
from constants import *
from Balloon import *

class BalloonManager():
    def __init__(self, window, max_width, max_height) -> None:
        self.window = window
        self.max_width = max_width
        self.max_height = max_height

    def start(self):
        self.balloon_list = []
        self.number_popped = 0
        self.number_missed = 0
        self.score = 0

        for i in range(N_BALLOONS):
            random_balloon = random.choice((BalloonSmall, BalloonMedium, BalloonLarge))
            balloon = random_balloon(self.window, self.max_width, self.max_height, i)
            self.balloon_list.append(balloon)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for balloon in reversed(self.balloon_list):
                was_hit, points = balloon.clicked_inside(event.pos)
                if was_hit:
                    if points > 0:
                        self.balloon_list.remove(balloon)
                        self.number_popped += 1
                        self.score += points
                        return

    def update(self):
        for balloon in self.balloon_list:
            status = balloon.update()
            if status == BALLOON_MISSED:
                self.balloon_list.remove(balloon)
                self.number_missed += 1

    def get_score(self):
        return self.score

    def get_count_popped(self):
        return self.number_popped

    def get_count_missed(self):
        return self.number_missed

    def draw(self):
        for balloon in self.balloon_list:
            balloon.draw()