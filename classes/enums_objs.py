from enum import Enum

from pygame import Vector2

from classes.character import Character
from classes.enemy import Enemy
from classes.enums import ClassChar, ClassEnemy
from classes.weapon import Weapon
from world import CEIL


class CharList(Enum):
    FIGHTER = Character(
        name="Fighter",
        hp=100,
        speed=250,
        scale=Vector2(CEIL, CEIL),
        weapon=Weapon(
            dmg=30,
            range=5,
            knockback=50,
            cooldown=100,
            speed=100
        ),
        class_char=ClassChar.MELEE
    )

    RANGER = Character(
        name="Ranger",
        hp=75,
        speed=200,
        scale=Vector2(CEIL, CEIL),
        weapon=Weapon(
            dmg=50,
            range=5000,
            knockback=100,
            cooldown=2000,
            speed=10000
        ),
        class_char=ClassChar.RANGE
    )


class EnemyList(Enum):
    ANGRY = Enemy(
        name="Angry",
        hp=60,
        speed=300,
        scale=Vector2(CEIL, CEIL),
        radius=300,
        type_enemy=ClassEnemy.MELEE
    )

    RANGER = Enemy(
        name="RangerEnemy",
        hp=30,
        speed=150,
        scale=Vector2(CEIL, CEIL),
        radius=1000,
        type_enemy=ClassEnemy.RANGE,
        weapon=Weapon(
            30, 10000, 30, 3000, 10000
        )
    )
