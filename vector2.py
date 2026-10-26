import math
import random


class Vector2:
    x: float = 0
    y: float = 0

    len = 0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

        self.len = math.sqrt(self.x**2 + self.y**2)

    def norm(self):
        if (self.len == 0) or (abs(self.len) == 1):
            return self
        else:
            return Vector2(self.x / self.len, self.y / self.len)

    def unpack(self):
        return (self.x, self.y)

    def __add__(self, vec):
        return Vector2(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector2(self.x - vec.x, self.y - vec.y)

    def __mul__(self, scalar: float):
        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float):
        return self*scalar

    def __truediv__(self, scalar: float):
        return Vector2(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar: float):
        return Vector2(self.x // scalar, self.y // scalar)

    @staticmethod
    def Randomize(
        a: int = -1,
        b: int = 1,
        mult: list[int] = [1, 1]
    ):
        return Vector2(random.randint(a*mult[0], b*mult[0]), random.randint(a*mult[1], b*mult[1]))
