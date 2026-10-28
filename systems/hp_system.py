from classes.enum_components import EC
from systems.system import System
from classes.object import Object


class HPSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        hp_comp = entity.GetComponent(EC.HP)
        if hp_comp != None:
            if hp_comp.value <= 0:
                Object.ALL.remove(entity)
