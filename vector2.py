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

    def __rmul__ (self, scalar: float):
        return self*scalar

    def __truediv__(self, scalar: float):
        return Vector2(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar: float):
        return Vector2(self.x // scalar, self.y // scalar)

    @staticmethod
    def Randomize():
        return Vector2(random.randint(-1, 1), random.randint(-1, 1))

VectorZero = Vector2(0, 0)
VectorUp = Vector2(0, -1)
VectorDown = Vector2(0, 1)
VectorLeft = Vector2(-1, 0)
VectorRight = Vector2(1, 0)