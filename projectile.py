class Projectile:
    ALL = []

    x, y = 0, 0
    id = 0
    speed = 0
    impulse = (0, 0)

    ID = 0

    def __init__(self, x, y, impulse, speed):
        self.x, self.y = x, y
        self.impulse = impulse
        self.id = Projectile.ID
        self.speed = speed

        Projectile.ID += 1

        Projectile.ALL.append(self)
