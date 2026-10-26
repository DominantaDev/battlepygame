from systems.system import System
from classes.object import Object
from components.velocity import Velocity
from components.transform import Transform
from components.movement import Movement
import world


class MovementSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        vel_comp = entity.GetComponent(Velocity)
        move_comp = entity.GetComponent(Movement)
        trans_comp = entity.GetComponent(Transform)

        if None in (vel_comp, move_comp, trans_comp):
            return

        trans_comp.pos += vel_comp.value.norm() * move_comp.speed * world.dt
        print(vel_comp.value)
