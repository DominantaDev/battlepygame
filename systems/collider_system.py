from classes.enum_components import EC
from classes.object import Object
from components.damage import Damage
from components.impulse import Impulse
from systems.system import System
from vector2 import Vector2


class ColliderSystem(System):
    @staticmethod
    def Apply(
            ent: Object
    ):
        vel_comp = ent.GetComponent(EC.VELOCITY)
        coll_comp = ent.GetComponent(EC.COLLIDER)
        trans_comp = ent.GetComponent(EC.TRANSFORM)
        ai_comp = ent.GetComponent(EC.AI)

        if None in (vel_comp, trans_comp, coll_comp):
            return

        if ai_comp:
            for i in ai_comp.victims:
                i_col_comp = i.GetComponent(EC.COLLIDER)
                i_trans_comp = i.GetComponent(EC.TRANSFORM)
                if None not in (i_col_comp, i_trans_comp):
                    if ColliderSystem.Chech(ent, i):
                        if not i.GetComponent(EC.HP).invul_status:
                            i.PinComponent(Damage(10))
                            i.AddComponent(
                                Impulse(i_trans_comp.pos-trans_comp.pos, 40))

    @staticmethod
    def Chech(
        first: Object,
        second: Object
    ):
        if None not in (first.GetComponent(EC.COLLIDER), second.GetComponent(EC.COLLIDER)):
            tr = first.GetComponent(EC.TRANSFORM)
            tr2 = second.GetComponent(EC.TRANSFORM)
            return all([(min(tr.pos.x+tr.scale.x, tr2.pos.x+tr2.scale.x) -
                         max(tr.pos.x, tr2.pos.x)) >= 0,
                        (min(tr.pos.y+tr.scale.y, tr2.pos.y+tr2.scale.y) -
                         max(tr.pos.y, tr2.pos.y)) >= 0])
        return False
