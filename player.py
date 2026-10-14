from entity import Entity
from enums import Action
from input_event import InputEvent
from vector2 import Vector2

import consts
import pygame

InputEvent("move_x", pygame.K_d, pygame.K_a)
InputEvent("move_y", pygame.K_s, pygame.K_w)

class Player(Entity):
    def __init__(self):
        super().__init__(
            buffer_actions=[],
            color=consts.RED,
            speed=25
        )

    def action_update(self, millsecs):
        self.Move(Vector2(InputEvent.getAxis("move_x", pygame.event), InputEvent.getAxis("move_y", pygame.event)))