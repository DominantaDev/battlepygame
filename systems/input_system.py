from components.input import Input
from components.velocity import Velocity
from input_event import InputEvent
from system import System
from classes.object import Object
from vector2 import Vector2


class InputSystem(System):
    def InputRegistry(
            entity: Object
    ):
        inp_comp = entity.GetComponent(Input)
        vel_comp = entity.GetComponent(Velocity)

        if None not in (inp_comp, vel_comp):
            vel_comp.value = Vector2(InputEvent.getAxis("move_x"),
                                     InputEvent.getAxis("move_y"))
