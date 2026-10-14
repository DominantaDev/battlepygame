import pygame

class InputEvent:
    ALL = []

    def __init__(self, 
                name,
                pos_key,
                neg_key = None
                ):
        self.name = name
        self.pos_key = pos_key
        self.neg_key = neg_key

        InputEvent.ALL.append(self)

    @staticmethod
    def getAxis(axis, event):
        for i in InputEvent.ALL:
            if axis == i.name:
                axis_obj = i
            else:
                raise ValueError(f"Нет оси с названием {axis}")
            
        if event.type == pygame.KEYDOWN:
            return
        
        print(f"{axis_obj.name} нажата кнопкой {event.key}")
        if event.key == axis_obj.pos_key:
            return 1
        elif event.key == axis_obj.neg_key:
            return -1
        else:
            return 0