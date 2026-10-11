from vector2 import Vector2
from entity import Entity

class Projectile(Entity):
    impulse = (0, 0)

    def __init__(self, pos: Vector2, impulse: Vector2, speed):
        super().__init__(pos, speed)
        
        self.impulse = impulse