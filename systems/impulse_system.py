from classes.enum_components import EC
from systems.system import System
from classes.object import Object


class ImpulseSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        trans_comp = entity.GetComponent(EC.TRANSFORM)
        imp_comp = entity.GetComponent(EC.IMPULSE)

        if imp_comp != None:
            trans_comp.pos += imp_comp.value.norm() * imp_comp.force
            entity.DeleteComponent(EC.IMPULSE)
