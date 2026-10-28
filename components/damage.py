from classes.enum_components import EC
from classes.enums import DamageType
from components.component import Component


class Damage(Component):
    _name = EC.DAMAGE

    def __init__(
            self,
            value: int = 10,
            dmg_type: DamageType = DamageType.PHYSICAL
    ):
        super().__init__(type(self)._name)

        self.value = value
        self.dmg_type = dmg_type
