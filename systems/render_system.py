import pygame
from classes.enum_components import EC
from classes.object import Object
import world
from systems.system import System


class RenderSystem(System):
    @staticmethod
    def Apply(
            ent: Object
    ):
        ren_comp = ent.GetComponent(EC.RENDER)
        trans_comp = ent.GetComponent(EC.TRANSFORM)
        if None in [ren_comp, trans_comp]:
            return

        pygame.draw.rect(world.screen, ren_comp.color, (trans_comp.pos.x,
                                                        trans_comp.pos.y, trans_comp.scale.x, trans_comp.scale.y))
