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

    # def normal(self):
    #     m = max(self.x, self.y)
    #     return Vector2(
    #         self.x if self.x == m else 0,
    #         self.y if self.y == m else 0
    #     )

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

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def copy(self):
        return Vector2(self.x, self.y)

    def dot(self, vec):
        return (self.x*vec.x)+(self.y*vec.y)

    def __lt__(self, vec):
        return self.x < vec.x and self.y < vec.y

    def __le__(self, vec):
        return self.x <= vec.x and self.y <= vec.y

    def __gt__(self, vec):
        return self.x > vec.x and self.y > vec.y

    def __ge__(self, vec):
        return self.x >= vec.x and self.y >= vec.y

    def __eq__(self, vec):
        return self.x == vec.x and self.y == vec.y

    def __ne__(self, vec):
        return self.x != vec.x and self.y != vec.y
