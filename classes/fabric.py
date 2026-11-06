from classes.character import Character
from classes.enemy import Enemy
from classes.enum_components import EC
from classes.enums import ColInterType, ClassEnemy
from classes.weapon import Weapon
from components.ai import AI
from components.collider import Collider
from components.info import Info
from components.lifetime import Lifetime
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
    def create_player(char: Character):
        char = char.value

        obj = Object()
        obj.AddComponents([
            Transform(Vector2(WIDTH//2, HEIGHT//2), char.scale),
            Movement(char.speed),
            HP(char.hp),
            Input(),
            Render(GREEN),
            Velocity(Vector2(0, 0)),
            Collider(),
            Material(ColInterType.NORMAL),
            Team(0),
            WeaponComp(char.weapon),
            Info(char.name, char.class_char)
        ])
        return obj

    def create_enemy(enemy_class: Enemy, player_obj):

        enemy_class = enemy_class.value
        obj = Object()
        obj.AddComponents([
            Transform(Vector2.Randomize(
                0, 1, [WIDTH, HEIGHT]), enemy_class.scale),
            Movement(enemy_class.speed),
            HP(enemy_class.hp),
            Render(RED),
            AI(enemy_class.radius, [player_obj]),
            Velocity(Vector2(0, 0)),
            Collider(),
            Material(ColInterType.NORMAL),
            Team(1),
            Info(enemy_class.name, enemy_class.type_enemy)
        ])
        if enemy_class.type_enemy == ClassEnemy.MELEE:
            obj.AddComponent(Sharpness(20, 20))
        else:
            obj.AddComponent(WeaponComp(enemy_class.weapon))
        return obj

    def create_bullet(
            parent_obj: Object,
            veloc: Vector2,
            weapon_obj: Weapon
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
            Team(parent_obj.GetComponent(EC.TEAM).num),
            Sharpness(20, 20),
            Info(f"Пуля {parent_obj.GetComponent(EC.INFO).name}",
                 parent_obj.GetComponent(EC.INFO).class_entity),
            Lifetime.init_distance(obj, parent_obj.GetComponent(
                EC.TRANSFORM).pos, parent_obj.GetComponent(EC.TRANSFORM).pos + veloc*weapon_obj.range, weapon_obj.speed)
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
            Material(ColInterType.NORMAL),
            Info("Стена", "Стена")
        ])
        return obj
