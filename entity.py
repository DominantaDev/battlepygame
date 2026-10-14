from vector2 import *
from moveable_object import MoveableObject
from random import choice
from enums import Action
import world
import consts

from projectile import Projectile

class Entity(MoveableObject):
    hp: int
    speed: int
    buffer_actions = []
    update_delta: float
    last_action: Action
    last_action_time: int
    target: Vector2

    def __init__(self, 
                pos=VectorZero, 
                speed=20, 
                hp=100, 
                buffer_actions=[],
                update_delta=100,
                target: Vector2 = VectorZero,
                color: tuple = consts.WHITE
                ):
        super().__init__(pos, speed, color)

        self.speed = speed
        self.buffer_actions = buffer_actions
        self.update_delta = update_delta
        self.target = target

        self.last_action_time = 0

    def action_update(self, millsecs):
        if not self.buffer_actions:
            return
        if (millsecs-self.last_action_time) >= self.update_delta:
            self.last_action_time = millsecs
            self.choice(self.buffer_actions)()
        else:
            return 

    def Move(self, direction: Vector2):
        self.pos += direction.norm() * self.speed * world.dt
        print(f"{type(self)} ({self.id}) переместился на {self.pos}")

    def Walk(self):
        self.Move(Vector2.Randomize())
        print(f"{type(self)} ({self.id}) гуляет")

    def Chase(self):
        self.Move(self.target.pos-self.pos)
        print(f"{type(self)} ({self.id}) преследует {type(self.target)} ({self.target.id})")

    def Shoot(self):
        Projectile(self.pos, (self.target.pos-self.pos).norm())
        print(f"{type(self)} ({self.id}) летит в направлении {type(self.target.impulse)}")