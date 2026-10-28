# Импорты
import pygame
from classes.enum_components import EC
from classes.fabric import Fabric
from classes.object import Object
import consts
from input_event import InputEvent
from systems.ai_system import AISystem
from systems.collider_system import ColliderSystem
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

for i in range(10, 20):
    Fabric.create_wall(Vector2(i*world.CEIL, 10))

start_game_time = pygame.time.get_ticks()

Timer(500, start_game_time, lambda: Fabric.create_wall(Vector2(
    random.randint(0, world.WIDTH), random.randint(0, world.HEIGHT))), infinity=True)
enemy_spawn_timer = Timer(3000, start_game_time,
                          lambda: Fabric.create_enemy(player), infinity=True)
while run:
    world.dt = clock.tick(world.FPS) / 1000
    world.now = pygame.time.get_ticks()-start_game_time
    Timer.UpdateAll(pygame.time.get_ticks()-start_game_time)

    # Обработка эвентов
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for ent in Object.ALL:
        InputSystem.Apply(ent)
        AISystem.Apply(ent)
        MovementSystem.Apply(ent)
        ColliderSystem.Apply(ent)
        DamageSystem.Apply(ent)
        ImpulseSystem.Apply(ent)
        HPSystem.Apply(ent)
        RenderSystem.Apply(ent)

    print(player.GetComponent(EC.HP).value)

    # Cycle-end
    pygame.display.update()
    world.screen.fill(world.screen_color)

pygame.quit()
