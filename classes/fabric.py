from classes.enum_components import EC
from classes.enums import ColInterType
from classes.weapon import Weapon
from components import team
from components.ai import AI
from components.collider import Collider
from components.material import Material
from components.render import Render
from components.hp import HP
from components.input import Input
from components.movement import Movement
from components.sharpness import Sharpness
from components.team import Team
from components.velocity import Velocity
from components.weapon_comp import WeaponComp
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
            Collider(),
            Material(ColInterType.NORMAL),
            Team(0),
            WeaponComp(Weapon(
                20, 50, 20, 150
            ))
        ])
        return obj

    def create_enemy(player_obj):
        obj = Object()
        obj.AddComponents([
            Transform(Vector2.Randomize(
                0, 1, [WIDTH, HEIGHT]), Vector2(CEIL, CEIL)),
            Movement(250),
            HP(100),
            Render(RED),
            AI(300, [player_obj]),
            Velocity(Vector2(0, 0)),
            Collider(),
            Material(ColInterType.NORMAL),
            Team(1),
            Sharpness(20, 20)
        ])
        return obj

    def create_bullet(
            parent_obj: Object,
            veloc: Vector2,
            team_num: int
    ):
        obj = Object()
        obj.AddComponents([
            Transform(parent_obj.GetComponent(
                EC.TRANSFORM).pos, Vector2(CEIL, CEIL)),
            Movement(600),
            Render(PINK),
            Velocity(veloc),
            Collider(),
            Material(ColInterType.FRAGILE),
            Team(team_num),
            Sharpness(20, 20)
        ])
        return obj

    def create_wall(
            pos: Vector2,
            size: Vector2 = Vector2(CEIL, CEIL)
    ):
        obj = Object()
        obj.AddComponents([
            Transform(pos, size),
            Render(WHITE),
            Collider(True),
            Material(ColInterType.NORMAL)
        ])
        return obj
