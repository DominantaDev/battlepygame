from classes.enum_components import EC
from classes.object import Object
from components.damage import Damage
from components.impulse import Impulse
from systems.system import System
from vector2 import Vector2
from world import CEIL


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
                    if ColliderSystem.Check(ent, i)[bool]:
                        if not i.GetComponent(EC.HP).invul_status:
                            i.PinComponent(Damage(10))
                            i.AddComponent(
                                Impulse(i_trans_comp.pos-trans_comp.pos, 40))

        for i in Object.ALL:
            if i.GetComponent(EC.COLLIDER).static:
                checked = ColliderSystem.Check(ent, i)
                if checked[bool]:
                    checked = checked[tuple]
                    trans_comp.pos -= min(
                        (
                            Vector2(checked[0].x, 0),
                            Vector2(checked[1].x, 0),
                            Vector2(0, checked[0].y),
                            Vector2(0, checked[1].y)
                        ),
                        key=lambda v: abs(v.x) + abs(v.y)
                    )

    @staticmethod
    def Check(
            first: Object,
            second: Object
    ):
        if None not in (first.GetComponent(EC.COLLIDER), second.GetComponent(EC.COLLIDER)):
            tr = first.GetComponent(EC.TRANSFORM)
            tr2 = second.GetComponent(EC.TRANSFORM)
            a = (
                tr.pos-(tr2.pos+tr2.scale),
                (tr.pos+tr.scale)-tr2.pos
            )
            z = 0
            return {
                tuple: a,
                bool: a[0]-Vector2(z, z) < Vector2(0, 0) < a[1]+Vector2(z, z)
            }
