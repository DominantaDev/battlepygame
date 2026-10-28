from classes.enum_components import EC
from components.component import Component
import consts


class Render(Component):
    _name = EC.RENDER

    def __init__(
            self,
            color: tuple = consts.WHITE
    ):
        super().__init__(type(self)._name)

        self.color = color
