from components.component import Component
from vector2 import *


class Velocity(Component):
    def __init__(
            self,
            value: Vector2 = None
    ):
        self.value = value
