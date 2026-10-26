from components.movement import Movement
from components.component import Component


class Object:
    ALL = []

    def __init__(
            self
    ):
        self.components = {}
        Object.ALL.append(self)

    def AddComponent(
            self,
            component: Component
    ):
        self.components[type(component)] = component

    def AddComponents(
        self,
        components: list[Component]
    ):
        for i in components:
            self.AddComponent(i)

    def DeleteComponent(
            self,
            component_type
    ):
        del self.components[component_type]

    def UpdateComponent(
        self,
        component
    ):
        component_type = type(component)
        if self.GetComponent(component_type) != 0:
            self.DeleteComponent(component_type)
        self.AddComponent(component)

    def GetComponent(
            self,
            component_type
    ):
        return self.components.get(component_type)

    def HasComponent(
            self,
            component_type
    ):
        return component_type in self.components
