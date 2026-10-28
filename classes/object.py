from classes.enum_components import EC
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
        self.components[component.name] = component

    def AddComponents(
        self,
        components: list[Component]
    ):
        for i in components:
            self.AddComponent(i)

    def DeleteComponent(
            self,
            component_type: EC
    ):
        del self.components[component_type]

    def GetComponent(
            self,
            component_type: EC
    ):
        return self.components.get(component_type)

    def HasComponent(
            self,
            component_type: EC
    ):
        return component_type in self.components.keys()

    def HasComponents(
            self,
            component_type_list: list[EC]
    ):
        return all([self.HasComponent(x) for x in component_type_list])
