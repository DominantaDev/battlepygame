from classes.enum_components import EC
from classes.fabric import Fabric
from classes.object import Object
from vector2 import Vector2


class Action:
    @staticmethod
    def Idle():
        pass

    @staticmethod
    def Chase(
            ent: Object,
            victim: Object
    ):
        ent.GetComponent(EC.VELOCITY).value = (victim.GetComponent(
            EC.TRANSFORM).pos - ent.GetComponent(EC.TRANSFORM).pos)

    @staticmethod
    def RunAway(
            ent: Object,
            victim: Object
    ):
        ent.GetComponent(EC.VELOCITY).value = (ent.GetComponent(
            EC.TRANSFORM).pos - victim.GetComponent(EC.TRANSFORM).pos)

    @staticmethod
    def Shoot(
            ent: Object,
            target: Vector2
    ):
        ent_trans = ent.GetComponent(EC.TRANSFORM)

        Fabric.create_bullet(ent, (target-ent_trans.pos).norm())
