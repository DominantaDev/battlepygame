from interval import Interval
from vector2 import Vector2


class Area:
    def __init__(
            self,
            min_pos: Vector2,
            max_pos: Vector2
    ):
        self.x_inter = Interval(min_pos.x, max_pos.x)
        self.y_inter = Interval(min_pos.y, max_pos.y)

    def within(
            self,
            dot: Vector2
    ):
        return self.x_inter.within(dot.x) and self.y_inter.within(dot.y)
