from classes.enum_components import EC
from components.component import Component

from classes.object import Object


class Info(Component):
    _name = EC.INFO

    def __init__(
            self,
            title: str
    ):
        super().__init__(type(self)._name)

        self.title = title
