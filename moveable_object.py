from vector2 import *
from object import Object
import consts

class MoveableObject(Object):
    ALL = []

    def __init__(self, pos=VectorZero, speed=20, color=consts.WHITE):
        super().__init__(pos=pos, color=color)
        self.speed = speed

        MoveableObject.ALL.append(self)