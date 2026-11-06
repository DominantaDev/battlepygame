from classes.enum_components import EC
from components.component import Component
from vector2 import Vector2


class Sharpness(Component):
    _title = EC.SHARPNESS

    def __init__(
        self,
        dmg: float = 20,
        imp: float = 20
    ):
        super().__init__(type(self)._title)

        self.dmg = dmg
        self.imp = imp
