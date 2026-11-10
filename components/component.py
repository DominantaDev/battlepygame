import copy

from classes.enum_components import EC
from classes.timer import Timer


class Component:
    def __init__(
            self,
            title: EC
    ):
        self.title = title

    def save(
            self,
            delay
    ):
        i = copy.deepcopy(self)
        Timer(delay, lambda: (self := copy.deepcopy(i)), False)
        return self
