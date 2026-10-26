from system import System
from classes.object import Object
from components.velocity import Velocity
from components.transform import Transform
from components.movement import Movement
import world


class MovementSystem(System):
    def MoveRegistry(
            entity: Object
    ):
        vel_comp = entity.GetComponent(Velocity)
        move_comp = entity.GetComponent(Movement)
        trans_comp = entity.GetComponent(Transform)

        if None not in (vel_comp, move_comp, trans_comp):
            trans_comp.pos += vel_comp.value.norm() * move_comp.speed * world.dt
