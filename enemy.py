from vector2 import Vector2
from entity import Entity

class Enemy(Entity):
    def __init__(self, pos: Vector2, speed):
        super().__init__(pos, speed)