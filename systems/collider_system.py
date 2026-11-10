from area import Area
from classes import enums_objs
from classes.enum_components import EC
from classes.enums import ColInterType
from classes.object import Object
from classes.timer import Timer
from components.damage import Damage
from components.effect_comp import EffectComp
from components.impulse import Impulse
from systems.system import System
from vector2 import Vector2
from world import CEIL
import world


class ColliderSystem(System):
    @staticmethod
    def Apply(
            ent: Object
    ):
        vel_comp = ent.GetComponent(EC.VELOCITY)
        coll_comp = ent.GetComponent(EC.COLLIDER)
        trans_comp = ent.GetComponent(EC.TRANSFORM)
        hp_comp = ent.GetComponent(EC.HP)
        ai_comp = ent.GetComponent(EC.AI)
        mat_comp = ent.GetComponent(EC.MATERIAL)
        team_comp = ent.GetComponent(EC.TEAM)
        sharp_comp = ent.GetComponent(EC.SHARPNESS)

        if None in (vel_comp, trans_comp, coll_comp):
            return

        for i in Object.ALL:
            if i.GetComponent(EC.COLLIDER).static:
                checked = ColliderSystem.Check(ent, i)
                if checked[bool]:
                    if mat_comp.intertype != ColInterType.GHOST:
                        if mat_comp.intertype == ColInterType.NORMAL:
                            checked = checked[Area]
                            trans_comp.pos -= min(
                                (
                                    Vector2(checked.x_inter.min_step, 0),
                                    Vector2(checked.x_inter.max_step, 0),
                                    Vector2(0, checked.y_inter.min_step),
                                    Vector2(0, checked.y_inter.max_step)
                                ),
                                key=lambda v: abs(v.x) + abs(v.y)
                            )
                        if mat_comp.intertype == ColInterType.FRAGILE:
                            ent.DELETEOBJ()
            if sharp_comp:
                i_hp_comp = i.GetComponent(EC.HP)
                i_team_comp = i.GetComponent(EC.TEAM)
                i_ai_comp = i.GetComponent(EC.AI)
                if None not in (i_hp_comp, i_team_comp):
                    if ColliderSystem.Check(ent, i)[bool] and team_comp.num != i_team_comp.num:
                        if not i_hp_comp.invul_status:
                            i.PinComponent(Damage(sharp_comp.dmg))
                            i.AddComponent(Impulse(i.GetComponent(
                                EC.TRANSFORM).pos-trans_comp.pos, sharp_comp.imp))
                            i.PinComponent(EffectComp(
                                enums_objs.EffectsEnum.BURNING, 5000, 5))
                            if None != i_ai_comp and not i_ai_comp.stunning:
                                i_ai_comp.stunning = True
                                Timer(1000, lambda comp=i_ai_comp: setattr(
                                    comp, "stunning", False))
                        if mat_comp.intertype == ColInterType.FRAGILE:
                            ent.DELETEOBJ()

    @staticmethod
    def Check(
            first: Object,
            second: Object
    ):
        if None not in (first.GetComponent(EC.COLLIDER), second.GetComponent(EC.COLLIDER)):
            tr = first.GetComponent(EC.TRANSFORM)
            tr2 = second.GetComponent(EC.TRANSFORM)
            mincov_dif = Area(
                tr.pos-(tr2.pos+tr2.scale),
                (tr.pos+tr.scale)-tr2.pos
            )
            if ColInterType.GHOST in (second.GetComponent(EC.MATERIAL).intertype, first.GetComponent(EC.MATERIAL).intertype):
                return {
                    Area: None,
                    bool: False
                }
            return {
                Area: mincov_dif,
                bool: mincov_dif.within(Vector2(0, 0))
            }
