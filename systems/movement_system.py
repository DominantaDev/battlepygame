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

        if vel_comp != None:
            trans_comp.pos += vel_comp.value.norm() * move_comp.speed * world.dt
