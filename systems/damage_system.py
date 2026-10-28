from classes.enum_components import EC
from classes.timer import Timer
import consts
from systems.system import System
from classes.object import Object
import world


class DamageSystem(System):
    @staticmethod
    def Apply(
            victim: Object
    ):
        dmg_comp = victim.GetComponent(EC.DAMAGE)
        hp_comp = victim.GetComponent(EC.HP)

        if not victim.HasComponents([EC.DAMAGE, EC.HP]):
            return

        if not hp_comp.invul_status:
            for i in victim.components[EC.DAMAGE]:
                hp_comp.value -= i.value
                victim.UnpinComponent(i)

            hp_comp.invul_status = True
            print("получил неузвимость")

            ren = victim.GetComponent(EC.RENDER)
            old_color = ren.color
            Timer(hp_comp.invul_frames, world.now,
                  lambda: (setattr(hp_comp, "invul_status", False),
                           setattr(ren, "color", old_color)))
            ren.color = consts.WHITE
