class Enemy:
    ID = 0
    ALL = []

    id = 0
    x, y = 0, 0
    speed = 0

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.id = Enemy.ID

        Enemy.ID += 1
        Enemy.ALL.append(self)