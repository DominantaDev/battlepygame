from system import System
from classes.object import Object
from components.damage import Damage
from components.damage import HP

class DamageSystem(System):
    def DamageRegistry(
            victim: Object
    ):
        dmg_comp = victim.GetComponent(Damage)

        if dmg_comp != None:
            victim.GetComponent(HP).value -= dmg_comp.value