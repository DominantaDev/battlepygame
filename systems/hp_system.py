from classes.enum_components import EC
import consts
from systems.system import System
from classes.object import Object
import world


class HPSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        hp_comp = entity.GetComponent(EC.HP)
        if hp_comp != None:
            if hp_comp.value <= 0:
                Object.ALL.remove(entity)
                world.screen_color = consts.WHITE
