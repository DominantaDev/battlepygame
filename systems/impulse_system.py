from systems.system import System
from classes.object import Object
from components.impulse import Impulse
from components.transform import Transform


class ImpulseSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        trans_comp = entity.GetComponent(Transform)
        imp_comp = entity.GetComponent(Impulse)

        if imp_comp != None:
            trans_comp.pos += imp_comp.value
