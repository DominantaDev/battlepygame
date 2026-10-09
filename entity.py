class Entity:
    ALL = []

    x = 0
    y = 0
    id = 0

    ID = 0

    def __init__(self, x, y):
        self.id = Entity.ID
        self.x = x
        self.y = y

        Entity.ID += 1

        Entity.ALL.append(self)