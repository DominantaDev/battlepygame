from classes.enum_components import EC
from components.component import Component

from classes.object import Object


class AI(Component):
    _name = EC.AI

    def __init__(
            self,
            radius: int = 100,
            victims: list[Object] = None,
            action=None
    ):
        super().__init__(type(self)._name)
        if victims is None:
            victims = []
        self.radius = radius
        self.victims = victims
        self.action = action
