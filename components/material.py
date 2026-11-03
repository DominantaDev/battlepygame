from classes.enum_components import EC
from components.component import Component
from classes.enums import ColInterType


class Material(Component):
    _name = EC.MATERIAL

    def __init__(
        self,
        intertype: ColInterType = ColInterType.NORMAL
    ):
        super().__init__(type(self)._name)

        self.intertype = intertype
