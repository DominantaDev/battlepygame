from system import System
from classes.object import Object
from components.damage import HP

class HPSystem(System):
    def DieRegistry(
            entity: Object
    ):
        hp_comp = entity.GetComponent(HP)
        if hp_comp != None:
            if hp_comp.value <= 0:
                del entity