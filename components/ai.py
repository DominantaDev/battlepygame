from components.component import Component

from classes.object import Object


class AI(Component):
    def __init__(
            self,
            radius: int = 100,
            victims: list[Object] = None,
            action=None
    ):
        if victims is None:
            victims = []
        self.radius = radius
        self.victims = victims
        self.action = action
