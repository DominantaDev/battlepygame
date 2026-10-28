from classes.enum_components import EC
from components.component import Component
from vector2 import *


class Movement(Component):
    _name = EC.MOVEMENT

    def __init__(
            self,
            speed: float = 200
    ):
        super().__init__(type(self)._name)

        self.speed = speed
