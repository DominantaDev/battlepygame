from vector2 import *
import consts


class Object:
    id_g: int
    id: int
    pos: Vector2
    color: tuple

    ID: int = 0
    ALL = []

    def __init__(self, pos=None, color=consts.WHITE):
        cls = type(self)

        self.id = cls.ID
        self.id_g = Object.ID
        self.pos = pos
        self.color = color

        cls.ID += 1
        cls.ALL.append(self)

        Object.ID += 1
        Object.ALL.append(self)

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.ID = 0
        cls.ALL = []
