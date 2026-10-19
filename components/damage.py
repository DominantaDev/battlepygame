from component import Component

class Damage(Component):
    def __init__(
            self,
            value: int = 10
    ):
        self.value = value