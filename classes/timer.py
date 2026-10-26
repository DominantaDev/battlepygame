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
    def UpdateAll(time: int):
        timers_exit = []
        """В МС!!!"""
        for i in Timer.ALL:
            i.now += world.dt
            if time-i.now >= i.delta:
                i.now = time
                timers_exit.append(i)
        return timers_exit
