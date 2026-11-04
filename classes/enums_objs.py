from enum import Enum

from pygame import Vector2

from classes.character import Character
from classes.enums import ClassChar
from classes.weapon import Weapon
from world import CEIL


class CharList(Enum):
    FIGHTER = Character(
        title="Fighter",
        hp=100,
        speed=250,
        scale=Vector2(CEIL, CEIL),
        weapon=Weapon(
            dmg=30,
            range=10,
            knockback=50,
            cooldown=100,
            speed=100
        ),
        class_char=ClassChar.MELEE
    )
