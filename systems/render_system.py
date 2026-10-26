import pygame
from classes.object import Object
from components.render import Render
from components.transform import Transform
import world
from systems.system import System


class RenderSystem(System):
    @staticmethod
    def Apply(
            ent: Object
    ):
        ren_comp = ent.GetComponent(Render)
        trans_comp = ent.GetComponent(Transform)
        if None in [ren_comp, trans_comp]:
            return

        pygame.draw.rect(world.screen, ren_comp.color, (trans_comp.pos.x,
                                                        trans_comp.pos.x, trans_comp.scale.x, trans_comp.scale.y))
