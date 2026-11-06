from classes.enum_components import EC
from components.component import Component
from vector2 import *


class Transform(Component):
    _title = EC.TRANSFORM

    def __init__(
            self,
            pos: Vector2 = None,
            scale: Vector2 = None
    ):
        super().__init__(type(self)._title)

        self.pos = pos
        self.scale = scale
