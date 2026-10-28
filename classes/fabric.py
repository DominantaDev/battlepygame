from classes.enum_components import EC
from components.ai import AI
from components.collider import Collider
from components.render import Render
from components.hp import HP
from components.input import Input
from components.movement import Movement
from components.velocity import Velocity
from vector2 import Vector2

from classes.object import Object
from components.transform import Transform
from world import *
from consts import *


class Fabric:
    @staticmethod
    def create_player():
        obj = Object()
        obj.AddComponents([
            Transform(Vector2(WIDTH//2, HEIGHT//2), Vector2(CEIL, CEIL)),
            Movement(200),
            HP(100),
            Input(),
            Render(GREEN),
            Velocity(Vector2(0, 0)),
            Collider()
        ])
        return obj

    def create_enemy(player_obj):
        obj = Object()
        obj.AddComponents([
            Transform(Vector2.Randomize(
                0, 1, [WIDTH, HEIGHT]), Vector2(CEIL, CEIL)),
            Movement(150),
            HP(50),
            Render(RED),
            AI(200, [player_obj]),
            Velocity(Vector2(0, 0)),
            Collider()
        ])
        return obj

    def create_bullet(
            parent_obj: Object,
            veloc: Vector2
    ):
        obj = Object()
        obj.AddComponents([
            Transform(parent_obj.GetComponent(
                EC.TRANSFORM).pos, Vector2(CEIL, CEIL)),
            Movement(600),
            Render(PINK),
            Velocity(veloc),
            Collider()
        ])
        return obj

    def create_wall(
            pos: Vector2
    ):
        obj = Object()
        obj.AddComponents([
            Transform(pos, Vector2(CEIL, CEIL)),
            Render(WHITE),
            Collider(True)
        ])
        return obj
