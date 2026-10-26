from components.component import Component
from vector2 import *


class Movement(Component):
    def __init__(
            self,
            speed: float = 200
    ):
        self.speed = speed
