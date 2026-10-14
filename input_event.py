import pygame
from vector2 import *

class InputEvent:
    ALL = []

    def __init__(self, 
                name,
                pos_key,
                neg_key = None
                ):
        self.name = name
        self.pos_key = pos_key
        self.neg_key = neg_key

        InputEvent.ALL.append(self)

    @staticmethod
    def getAxis(axis):
        axis_obj = None

        for i in InputEvent.ALL:
            if axis == i.name:
                axis_obj = i
                break

        if axis_obj is None:
            raise ValueError(f"Нет оси с названием {axis}")

        keys = pygame.key.get_pressed()

        return int(keys[axis_obj.pos_key]) - int(keys[axis_obj.neg_key])