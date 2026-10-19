from component import Component

class HP(Component):
    def __init__(
            self,
            value: int = 100,
    ):
        self.value = value