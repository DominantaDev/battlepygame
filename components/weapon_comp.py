from classes.enum_components import EC
from classes.weapon import Weapon
from components.component import Component

from classes.object import Object


class WeaponComp(Component):
    _title = EC.WEAPONCOMP

    def __init__(
            self,
            main: Weapon
    ):
        super().__init__(type(self)._title)

        self.main = main
