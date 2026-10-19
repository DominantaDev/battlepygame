from components.hp import HP
from system import System
from classes.object import Object
from classes.action import Action
from components.ai import AI
from components.transform import Transform


class AISystem(System):
    def AIApply(
            entity: Object
    ):
        ai_comp = entity.GetComponent(AI)
        trans_comp = entity.GetComponent(Transform)
        hp_comp = entity.GetComponent(HP)

        ai_comp.action = Action.Idle

        if ai_comp != None:
            for ent in Object.ALL:
                if ent.HasComponent(Transform):
                    if ent in ai_comp.victims:
                        if (ent.GetComponent(Transform).pos - trans_comp.pos).len <= ai_comp.radius:
                            if hp_comp.value <= 25:
                                Action.RunAway()
                                return

                            Action.Chase(entity, ent)
                            return
