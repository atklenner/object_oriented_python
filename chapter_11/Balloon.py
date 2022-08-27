import pygame
import random
from pygame.locals import *
import pygwidgets
from constants import *
from abc import ABC, abstractmethod
from pathlib import Path
BASE_PATH = str(Path(__file__).resolve().parent)

class Balloon(ABC):
    pop_sound_loaded = False
    pop_sound = None

    @abstractmethod
    def __init__(self, window, max_width, max_height, ID, image, size, points, speed_y) -> None:
        self.window = window
        self.ID = ID
        self.balloon_image = image
        self.size = size
        self.points = points
        self.speed_y = speed_y
        if not Balloon.pop_sound_loaded:
            Balloon.pop_sound_loaded = True
            Balloon.pop_sound = pygame.mixer.Sound(BASE_PATH + "/sounds/balloonPop.wav")
        
        balloon_rect = self.balloon_image.getRect()
        self.width = balloon_rect.width
        self.height = balloon_rect.height
        self.x = random.randrange(max_width - self.width)
        self.y = max_height + random.randrange(75)
        self.balloon_image.setLoc((self.x, self.y))

    def clicked_inside(self, mouse_point):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if rect.collidepoint(mouse_point):
            Balloon.pop_sound.play()
            return True, self.points
        else:
            return False

    def update(self):
        self.y -= self.speed_y
        self.balloon_image.setLoc((self.x, self.y))
        if self.y < -self.height:
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloon_image.draw()

    def __del__(self):
        print(self.size, "Balloon", self.ID, "is going away")

class BalloonSmall(Balloon):
    balloon_image = pygame.image.load(BASE_PATH + "/images/redBalloonSmall.png")
    def __init__(self, window, max_width, max_height, ID) -> None:
        image = pygwidgets.Image(window, (0, 0), BalloonSmall.balloon_image)
        super().__init__(window, max_width, max_height, ID, image, "Small", 30, 3.1)

class BalloonMedium(Balloon):
    balloon_image = pygame.image.load(BASE_PATH + "/images/redBalloonMedium.png")
    def __init__(self, window, max_width, max_height, ID) -> None:
        image = pygwidgets.Image(window, (0, 0), BalloonMedium.balloon_image)
        super().__init__(window, max_width, max_height, ID, image, "Medium", 20, 2.2)

class BalloonLarge(Balloon):
    balloon_image = pygame.image.load(BASE_PATH + "/images/redBalloonLarge.png")
    def __init__(self, window, max_width, max_height, ID) -> None:
        image = pygwidgets.Image(window, (0, 0), BalloonLarge.balloon_image)
        super().__init__(window, max_width, max_height, ID, image, "Large", 10, 1.5)