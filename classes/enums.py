from enum import Enum, auto


class DamageType(Enum):
    PHYSICAL = auto()
    MAGIC = auto()
    RANGED = auto()


class ColInterType(Enum):
    FRAGILE = auto()
    NORMAL = auto()
    GHOST = auto()


class ClassChar(Enum):
    MELEE = "Melee"
    RANGE = "Range"
    SUPPORT = "Support"


class ClassEnemy(Enum):
    MELEE = "Melee"
    RANGE = "Range"
