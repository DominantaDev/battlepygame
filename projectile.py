from vector2 import *
import consts
from moveable_object import MoveableObject

class Projectile(MoveableObject):
    impulse: Vector2

    def __init__(self, pos: Vector2 = VectorZero, impulse: Vector2 = VectorZero, speed: int = 20):
        super().__init__(pos=pos, speed=speed, color=consts.GREEN)

        self.impulse = impulse