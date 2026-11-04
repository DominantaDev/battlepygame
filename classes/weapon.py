from classes.object import Object


class Weapon:
    def __init__(
        self,
        dmg: float = 10,
        range: float = 50,
        knockback: float = 20,
        cooldown: float = 300
    ):
        self.dmg = dmg
        self.range = range
        self.knockback = knockback
        self.cooldown = cooldown

        self.done = True
