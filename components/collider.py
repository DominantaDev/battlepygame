from classes.enum_components import EC
from components.component import Component


class Collider(Component):
    _title = EC.COLLIDER

    def __init__(
        self,
        static: bool = False
    ):
        super().__init__(type(self)._title)

        self.static = static
