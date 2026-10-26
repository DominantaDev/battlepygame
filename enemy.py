from vector2 import *
from entity import Entity
from random import choice
import consts


class Enemy(Entity):
    def __init__(self, pos: Vector2 = None, target=None, speed: int = 50, damage: int = 10, buffer_actions=[]):
        super().__init__(pos=pos, speed=speed, buffer_actions=buffer_actions, target=target)
        self.damage = damage
        self.buffer_actions = [self.Walk, self.Shoot, self.Chase]
