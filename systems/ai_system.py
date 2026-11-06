from classes.enum_components import EC
from classes.enums import ClassEnemy
from classes.fabric import Fabric
from classes.timer import Timer
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
        info_comp = entity.GetComponent(EC.INFO)

        if None in (ai_comp, trans_comp, hp_comp, vel_comp, info_comp):
            return

        ai_comp.action = Action.Idle
        vel_comp.value = Vector2(0, 0)

        if not ai_comp.stunning:
            for vict in Object.ALL:
                if vict.HasComponent(EC.TRANSFORM):
                    if vict in ai_comp.victims:
                        if (vict.GetComponent(EC.TRANSFORM).pos - trans_comp.pos).len <= ai_comp.radius:
                            if hp_comp.value <= 25:
                                Action.RunAway(entity, vict)
                                return
                            if info_comp.class_entity == ClassEnemy.MELEE:
                                Action.Chase(entity, vict)
                                return
                            elif info_comp.class_entity == ClassEnemy.RANGE:
                                weap_comp = entity.GetComponent(EC.WEAPONCOMP)
                                if weap_comp.main.done:
                                    Fabric.create_bullet(entity, (vict.GetComponent(
                                        EC.TRANSFORM).pos - trans_comp.pos).norm(), entity.GetComponent(EC.WEAPONCOMP).main)
                                    weap_comp.main.done = False
                                    Timer(weap_comp.main.cooldown,
                                          lambda: setattr(weap_comp.main, "done", True))
                                    return
