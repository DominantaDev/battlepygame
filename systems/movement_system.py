from classes.enum_components import EC
from systems.system import System
from classes.object import Object
import world


class MovementSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        vel_comp = entity.GetComponent(EC.VELOCITY)
        move_comp = entity.GetComponent(EC.MOVEMENT)
        trans_comp = entity.GetComponent(EC.TRANSFORM)

        if None in (vel_comp, move_comp, trans_comp):
            return

        trans_comp.pos += vel_comp.value.norm() * move_comp.speed * world.dt
