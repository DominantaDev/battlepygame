class Entity:
    Entities = []

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

        Entity.Entities.append(self)