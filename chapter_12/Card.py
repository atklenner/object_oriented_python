import pygame
import pygwidgets

class Card():
    BACK_OF_CARD_IMAGE = 

    def __init__(self, window, rank, suit, value) -> None:
        self.window = window
        self.rank = rank
        self.suit = suit
        self.card_name = rank + " of " + suit
        self.value = value
        file_name = "/images/" + self.card_name + ".png"
        self.images = 

    def conceal(self):
        pass

    def reveal(self):
        pass

    def get_name(self):
        return self.card_name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_loc(self, loc):
        pass

    def get_loc(self):
        pass

    def draw(self):
        self.images.draw()