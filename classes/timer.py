import world


class Timer:
    ALL = []

    def __init__(
            self,
            delta: int,
            func,
            infinity: bool = False
    ):
        """delta в миллисекундах(с/1000) DT В СЕКУНДАХ"""
        self.delta = delta
        self.now = world.now
        self.func = func
        self.infinity = infinity

        Timer.ALL.append(self)

    @staticmethod
    def UpdateAll(time: int):
        """В МС!!!"""
        for i in Timer.ALL.copy():
            if time-i.now >= i.delta:
                i.func()
                if i.infinity:
                    Timer(i.delta, i.func, i.infinity)
                Timer.ALL.remove(i)
                del i
