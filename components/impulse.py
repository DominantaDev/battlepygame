from component import Component
from vector2 import *


class Impulse(Component):
    def __init__(
            self,
            value: Vector2 = None
    ):
        self.value = value
