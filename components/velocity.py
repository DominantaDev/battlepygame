from classes.enum_components import EC
from components.component import Component
from vector2 import *


class Velocity(Component):
    _title = EC.VELOCITY

    def __init__(
            self,
            value: Vector2 = None
    ):
        super().__init__(type(self)._title)

        self.value = value
