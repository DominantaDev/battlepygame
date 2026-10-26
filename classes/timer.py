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
        self.run = False

        Timer.ALL.append(self)

    @staticmethod
    def UpdateAll(time: int):
        """В МС!!!"""
        for i in Timer.ALL:
            # print(f"{time}-{i.now} >= {i.delta} >>> {i.run}")
            if time-i.now >= i.delta:
                i.now = time
                i.run = True
            else:
                i.run = False
