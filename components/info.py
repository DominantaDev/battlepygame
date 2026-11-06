from classes.enum_components import EC
from components.component import Component

from classes.object import Object


class Info(Component):
    _title = EC.INFO

    def __init__(
            self,
            name: str,
            class_entity: str
    ):
        super().__init__(type(self)._title)

        self.name = name
        self.class_entity = class_entity
