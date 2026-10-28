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

        if None in (dmg_comp, hp_comp):
            return

        if not hp_comp.invul_status:
            hp_comp.value -= dmg_comp.value
            victim.DeleteComponent(EC.DAMAGE)
            hp_comp.invul_status = True

            ren = victim.GetComponent(EC.RENDER)
            print(ren.color)
            old_color = ren.color
            Timer(hp_comp.invul_frames, world.now,
                  lambda: (setattr(hp_comp, "invul_status", False),
                           setattr(ren, "color", old_color)))
            ren.color = consts.WHITE
