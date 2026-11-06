from classes.enum_components import EC
from components.component import Component
from vector2 import *


class Impulse(Component):
    _title = EC.IMPULSE

    def __init__(
            self,
            value: Vector2 = None,
            force: float = 10
    ):
        super().__init__(type(self)._title)
        self.value = value
        self.force = force
