class Timer:
    ALL = []

    def __init__(
            self,
            delta: int,
            now: int,
            func,
            infinity: bool = False
    ):
        """delta в миллисекундах(с/1000) DT В СЕКУНДАХ"""
        self.delta = delta
        self.now = now
        self.func = func
        self.infinity = infinity

        Timer.ALL.append(self)

    @staticmethod
    def UpdateAll(time: int):
        """В МС!!!"""
        for i in Timer.ALL.copy():
            # print(f"{time}-{i.now} >= {i.delta} >>> {i.run}")
            if time-i.now >= i.delta:
                i.now = time
                i.func()
                if i.infinity:
                    Timer(i.delta, i.now, i.func, i.infinity)
                Timer.ALL.remove(i)
                del i
