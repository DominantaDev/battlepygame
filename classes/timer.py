import world


class Timer:
    ALL = []

    def __init__(
            self,
            delta: int
    ):
        """delta в миллисекундах(с/1000) DT В СЕКУНДАХ"""
        self.delta = delta
        self.now = 0

        Timer.ALL.append(self)

    @staticmethod
    def UpdateAll():
        for i in Timer.ALL:
            i.now += world.dt
            if
