from classes.action import Action
from classes.enum_components import EC
from input_event import InputEvent
from systems.system import System
from classes.object import Object
from vector2 import Vector2


class InputSystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        inp_comp = entity.GetComponent(EC.INPUT)
        vel_comp = entity.GetComponent(EC.VELOCITY)

        sht_x_ev = InputEvent.getAxis("shoot_x")
        sht_y_ev = InputEvent.getAxis("shoot_y")

        if None in (inp_comp, vel_comp):
            return

        vel_comp.value = Vector2(InputEvent.getAxis("move_x"),
                                 InputEvent.getAxis("move_y"))
        if sht_x_ev != 0 or sht_y_ev != 0:
            Action.Shoot(entity, entity.GetComponent(EC.TRANSFORM).pos + Vector2(
                sht_x_ev,
                sht_y_ev
            ))
