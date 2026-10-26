from component import Component
from vector2 import *


class Transform(Component):
    def __init__(
            self,
            pos: Vector2 = None,
            scale: Vector2 = None
    ):
        self.pos = pos
        self.scale = scale
