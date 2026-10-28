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

    def PinComponent(
            self,
            component: Component
    ):
        self.components.setdefault(component.name, []).append(component)

    def UnpinComponent(
            self,
            component: Component
    ):
        if component in self.components[component.name]:
            self.components[component.name].remove(component)

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
        if type(self.components.get(component_type)) == list:
            return bool(self.components[component_type])
        return component_type in self.components.keys()

    def HasComponents(
            self,
            component_type_list: list[EC]
    ):
        return all([self.HasComponent(x) for x in component_type_list])
