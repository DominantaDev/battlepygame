from classes.enum_components import EC
from components.component import Component
from classes.enums import ColInterType


class Material(Component):
    _title = EC.MATERIAL

    def __init__(
        self,
        intertype: ColInterType = ColInterType.NORMAL
    ):
        super().__init__(type(self)._title)

        self.intertype = intertype
