from classes.fabric import Fabric
from classes.object import Object
from components.movement import Movement
from components.velocity import Velocity
from components.transform import Transform
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
        ent.GetComponent(Velocity).value = (victim.GetComponent(
            Transform).pos - ent.GetComponent(Transform).pos)

    @staticmethod
    def RunAway(
            ent: Object,
            victim: Object
    ):
        ent.GetComponent(Velocity).value = (ent.GetComponent(
            Transform).pos - victim.GetComponent(Transform).pos)

    @staticmethod
    def Shoot(
            ent: Object,
            target: Vector2
    ):
        ent_trans = ent.GetComponent(Transform)
        targ_trans = target.GetComponent(Transform)

        Fabric.create_bullet(ent, (targ_trans-ent_trans).norm())
