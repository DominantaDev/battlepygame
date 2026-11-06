from classes.entity import Entity
from classes.enums import ClassEnemy
from classes.weapon import Weapon
from vector2 import Vector2


class Enemy(Entity):
    def __init__(
        self,
        name: str,
        hp: float,
        speed: float,
        scale: Vector2,
        radius: float,
        type_enemy: ClassEnemy,
        weapon: Weapon = Weapon()
    ):
        super().__init__(name, hp, speed, scale, weapon)

        self.radius = radius
        self.type_enemy = type_enemy
