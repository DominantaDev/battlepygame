from classes.enums import ClassChar
from classes.weapon import Weapon
from vector2 import Vector2


class Character:
    def __init__(
        self,
        title: str,
        hp: float,
        speed: float,
        scale: Vector2,
        weapon: Weapon,
        class_char: ClassChar
    ):
        self.title = title
        self.hp = hp
        self.speed = speed
        self.scale = scale
        self.weapon = weapon
        self.class_char = class_char
