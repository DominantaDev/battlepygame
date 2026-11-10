from components.component import Component


class Effect:
    def __init__(
            self,
            name: str,
            action,
            comp: Component = None,
            once: bool = True
    ):
        self.name = name
        self.action = action
        self.comp = comp
        self.once = once
