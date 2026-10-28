from classes.enum_components import EC
from components.component import Component


class Collider(Component):
    _name = EC.COLLIDER

    def __init__(
        self
    ):
        super().__init__(type(self)._name)
