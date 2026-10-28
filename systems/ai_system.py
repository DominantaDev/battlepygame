from classes.enum_components import EC
from systems.system import System
from classes.object import Object
from classes.action import Action
from vector2 import Vector2


class AISystem(System):
    @staticmethod
    def Apply(
            entity: Object
    ):
        ai_comp = entity.GetComponent(EC.AI)
        trans_comp = entity.GetComponent(EC.TRANSFORM)
        hp_comp = entity.GetComponent(EC.HP)
        vel_comp = entity.GetComponent(EC.VELOCITY)

        if None in (ai_comp, trans_comp, hp_comp, vel_comp):
            return

        ai_comp.action = Action.Idle
        vel_comp.value = Vector2(0, 0)

        for vict in Object.ALL:
            if vict.HasComponent(EC.TRANSFORM):
                if vict in ai_comp.victims:
                    if (vict.GetComponent(EC.TRANSFORM).pos - trans_comp.pos).len <= ai_comp.radius:
                        if hp_comp.value <= 25:
                            Action.RunAway(entity, vict)
                            return

                        Action.Chase(entity, vict)
                        return
