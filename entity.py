from vector2 import Vector2
from object import Object

class Entity(Object):
    speed: int

    def __init__(self, pos, speed):
        super().__init__(pos)

        self.speed = speed