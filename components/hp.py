from classes.enum_components import EC
from components.component import Component


class HP(Component):
    _title = EC.HP

    def __init__(
            self,
            value: int = 100,
            invul_frames: int = 1000
    ):
        """invul_frames в мс"""
        super().__init__(type(self)._title)

        self.value = value
        self.invul_frames = invul_frames
        self.invul_status = False
