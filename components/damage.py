from classes.enum_components import EC
from components.component import Component


class Damage(Component):
    _name = EC.DAMAGE

    def __init__(
            self,
            value: int = 10
    ):
        super().__init__(type(self)._name)

        self.value = value
