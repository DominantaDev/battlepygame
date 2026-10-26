from components.hp import HP
from components.velocity import Velocity
from system import System
from classes.object import Object
from classes.action import Action
from components.ai import AI
from components.transform import Transform
from vector2 import Vector2


class AISystem(System):
    def AIApply(
            entity: Object
    ):
        if ai_comp == None:
            return

        ai_comp = entity.GetComponent(AI)
        trans_comp = entity.GetComponent(Transform)
        hp_comp = entity.GetComponent(HP)

        ai_comp.action = Action.Idle
        entity.UpdateComponent(Velocity(Vector2(0, 0)))

        for vict in Object.ALL:
            if vict.HasComponent(Transform):
                if vict in ai_comp.victims:
                    if (vict.GetComponent(Transform).pos - trans_comp.pos).len <= ai_comp.radius:
                        if hp_comp.value <= 25:
                            Action.RunAway(entity, vict)
                            return

                        Action.Chase(entity, vict)
                        return
