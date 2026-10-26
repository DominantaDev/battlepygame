from components.input import Input
from components.velocity import Velocity
from input_event import InputEvent
from systems.system import System
from classes.object import Object
from vector2 import Vector2


class InputSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        inp_comp = entity.GetComponent(Input)
        vel_comp = entity.UpdateComponent(Velocity)

        if None in (inp_comp, vel_comp):
            return

        print(InputEvent.getAxis("move_x"), InputEvent.getAxis("move_y"))
        vel_comp.value = Vector2(InputEvent.getAxis("move_x"),
                                 InputEvent.getAxis("move_y"))
