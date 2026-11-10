from classes.effect import Effect
from classes.enum_components import EC
from components.component import Component


class EffectComp(Component):
    _title = EC.EFFECT

    def __init__(
            self,
            template: Effect,
            duration: int,
            force: float,
            infinity: bool = False
    ):
        super().__init__(type(self)._title)

        self.template = template
        self.duration = duration
        self.force = force
        self.infinity = infinity

        self.done = False
