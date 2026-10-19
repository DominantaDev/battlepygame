from classes.object import Object
from components.velocity import Velocity
from components.transform import Transform

class Action:
    def Idle():
        pass

    def Chase(
            ent: Object,
            victim: Object
    ):
        ent.GetComponent(Velocity).value = (victim.GetComponent(Transform).pos - ent.GetComponent(Transform).pos)

    def RunAway(
            ent: Object,
            victim: Object
    ):
        ent.GetComponent(Velocity).value = (ent.GetComponent(Transform).pos - victim.GetComponent(Transform).pos)