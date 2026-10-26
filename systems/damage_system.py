from systems.system import System
from classes.object import Object
from components.damage import Damage
from components.hp import HP


class DamageSystem(System):
    @staticmethod
    def Apply(
            victim: Object
    ):
        dmg_comp = victim.GetComponent(Damage)

        if dmg_comp != None:
            victim.GetComponent(HP).value -= dmg_comp.value
