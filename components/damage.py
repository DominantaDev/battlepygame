from classes.enum_components import EC
from classes.enums import DamageType
from components.component import Component


class Damage(Component):
    _title = EC.DAMAGE

    def __init__(
            self,
            value: int = 10,
            dmg_type: DamageType = DamageType.PHYSICAL,
            invul_on: bool = True
    ):
        super().__init__(type(self)._title)

        self.value = value
        self.dmg_type = dmg_type
        self.invul_on = invul_on
