class Interval:
    def __init__(
        self,
        min_step: float,
        max_step: float
    ):
        self.min_step = min_step
        self.max_step = max_step

    def within(
            self,
            value: float
    ):
        return (self.min_step <= value <= self.max_step)
