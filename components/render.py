from classes.enum_components import EC
from components.component import Component
import consts


class Render(Component):
    _title = EC.RENDER

    def __init__(
            self,
            color: tuple = consts.WHITE
    ):
        super().__init__(type(self)._title)

        self.color = color
