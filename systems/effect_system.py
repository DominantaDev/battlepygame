from classes.enum_components import EC
from classes.timer import Timer
from systems.system import System
from classes.object import Object
import world


class EffectSystem(System):
    @staticmethod
    def Apply(
            victim: Object
    ):
        eff_comp = victim.GetComponent(EC.EFFECT)

        if None == (eff_comp):
            return

        for eff in eff_comp:
            if not eff.done:
                eff.template.value.comp.copy() if eff.template.value.comp else None
                Timer(eff.duration, lambda: victim.UnpinComponent(
                    eff), eff.infinity)
                eff.done = True
                if eff.template.value.once:
                    eff.template.value.action(victim, eff.force*world.dt)
                # print(eff.duration, eff.force, eff.infinity)
            if not eff.template.value.once:
                eff.template.value.action(victim, eff.force*world.dt)
