from classes.enum_components import EC
from components.component import Component


class Team(Component):
    _name = EC.TEAM

    def __init__(
        self,
        num: int
    ):
        """color буквально цвет команды"""
        super().__init__(type(self)._name)

        self.num = num
