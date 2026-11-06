from classes.entity import Entity
from classes.enums import ClassChar
from classes.weapon import Weapon
from vector2 import Vector2


class Character(Entity):
    def __init__(
        self,
        name: str,
        hp: float,
        speed: float,
        scale: Vector2,
        weapon: Weapon,
        class_char: ClassChar
    ):
        super().__init__(name, hp, speed, scale, weapon)

        self.class_char = class_char
