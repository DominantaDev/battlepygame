from classes.enum_components import EC
from components.component import Component
from vector2 import *


class Input(Component):
    _name = EC.INPUT

    def __init__(
            self
    ):
        super().__init__(type(self)._name)
