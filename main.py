# Импорты
import pygame
from classes.fabric import Fabric
from classes.object import Object
from components.ai import AI
from components.velocity import Velocity
import consts
from input_event import InputEvent
from systems.ai_system import AISystem
from systems.damage_system import DamageSystem
from systems.hp_system import HPSystem
from systems.impulse_system import ImpulseSystem
from systems.input_system import InputSystem
from systems.movement_system import MovementSystem
from systems.render_system import RenderSystem
import world
from classes.timer import Timer
from vector2 import *

# Настройки
pygame.init()
world.screen = pygame.display.set_mode((world.WIDTH, world.HEIGHT))
pygame.display.set_caption('ZMEYAAAA')
clock = pygame.time.Clock()

player = Fabric.create_player()

InputEvent("move_x", pygame.K_d, pygame.K_a)
InputEvent("move_y", pygame.K_s, pygame.K_w)

InputEvent("shoot_x", pygame.K_RIGHT, pygame.K_LEFT)
InputEvent("shoot_y", pygame.K_DOWN, pygame.K_UP)

# Основной цикл
run = True
world.dt = 0

enemy_spawn_timer = Timer(3000)

start_game_time = pygame.time.get_ticks()
while run:
    world.dt = clock.tick(world.FPS) / 1000
    timers_exit = Timer.UpdateAll(pygame.time.get_ticks()-start_game_time)
    # Обработка эвентов
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if enemy_spawn_timer.run:
        Fabric.create_enemy(player)

    for ent in Object.ALL:
        InputSystem.Apply(ent)
        AISystem.Apply(ent)
        MovementSystem.Apply(ent)
        DamageSystem.Apply(ent)
        ImpulseSystem.Apply(ent)
        HPSystem.Apply(ent)
        RenderSystem.Apply(ent)

    # Cycle-end
    pygame.display.update()
    world.screen.fill(consts.BLACK)

pygame.quit()
