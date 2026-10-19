from component import Component
from vector2 import *

class Transform(Component):
    def __init__(
            self,
            pos: Vector2 = VectorZero,
            scale: Vector2 = Vector2(10, 10)
    ):
        self.pos = pos
        self.scale = scale