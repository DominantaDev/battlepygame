from classes.weapon import Weapon
from vector2 import Vector2


class Entity:
    def __init__(
        self,
        name: str,
        hp: float,
        speed: float,
        scale: Vector2,
        weapon: Weapon
    ):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.scale = scale
        self.weapon = weapon
