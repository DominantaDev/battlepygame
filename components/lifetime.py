from classes.enum_components import EC
from classes.object import Object
from classes.timer import Timer
from components.component import Component
from vector2 import Vector2


class Lifetime(Component):
    _title = EC.LIFETIME

    def __init__(
            self,
            value: float,
            parent: Object
    ):
        super().__init__(type(self)._title)

        self.value = value

        Timer(value, lambda: parent.DELETEOBJ())

    @staticmethod
    def init_distance(
            parent: Object,
            first_pos: Vector2,
            last_pos: Vector2,
            speed: float
    ):
        # print(f"{(last_pos-first_pos).len/speed} секунд ибо speed={speed}, дистанция={(last_pos-first_pos).len}")
        return Lifetime(((last_pos-first_pos).len/speed)*1000, parent)
