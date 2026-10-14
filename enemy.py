from vector2 import *
from entity import Entity
from enums import *
from random import choice
import consts

class Enemy(Entity):
    def __init__(self, pos: Vector2 = VectorZero, speed: int = 100, damage: int = 10, buffer_actions=[]):
        super().__init__()
        self.damage = damage
        self.buffer_actions = [self.Walk, self.Shoot, self.Chase]