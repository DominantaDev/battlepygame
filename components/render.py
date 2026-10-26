from components.component import Component
import consts


class Render(Component):
    def __init__(
            self,
            color: tuple = consts.WHITE
    ):
        self.color = color
