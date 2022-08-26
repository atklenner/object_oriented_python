import pygame
import random
from pygame.locals import *
import pygwidgets
from constants import *
from abc import ABC, abstractmethod

class Balloon(ABC):
    def __init__(self) -> None:
        pass

class BalloonSmall(Balloon):
    def __init__(self) -> None:
        super().__init__()

class BalloonMedium(Balloon):
    def __init__(self) -> None:
        super().__init__()

class BalloonLarge(Balloon):
    def __init__(self) -> None:
        super().__init__()