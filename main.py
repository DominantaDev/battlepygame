# Импорты
import pygame
from classes.enum_components import *
from classes.enums_objs import CharList, EnemyList
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

player = Fabric.create_player(random.choice([i for i in CharList]))

InputEvent("move_x", pygame.K_d, pygame.K_a)
InputEvent("move_y", pygame.K_s, pygame.K_w)

InputEvent("shoot_x", pygame.K_RIGHT, pygame.K_LEFT)
InputEvent("shoot_y", pygame.K_DOWN, pygame.K_UP)

# Основной цикл
run = True
world.dt = 0

Fabric.create_wall(Vector2(50*world.CEIL, 50*world.CEIL),
                   Vector2(world.CEIL*20, world.CEIL*15))
Fabric.create_wall(
    Vector2(0, 0-world.CEIL*10),
    Vector2(world.WIDTH, world.CEIL*10)
)
Fabric.create_wall(
    Vector2(0, world.HEIGHT),
    Vector2(world.WIDTH, world.CEIL*10)
)
Fabric.create_wall(
    Vector2(0-world.CEIL*10, 0),
    Vector2(world.CEIL*10, world.HEIGHT)
)
Fabric.create_wall(
    Vector2(world.WIDTH, 0),
    Vector2(world.CEIL*10, world.HEIGHT)
)

start_game_time = pygame.time.get_ticks()
world.now = start_game_time

enemy_spawn_timer = Timer(1500,
                          lambda: Fabric.create_enemy(random.choice([i for i in EnemyList]), player), infinity=True)

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

    # Cycle-end
    pygame.display.update()
    world.screen.fill(world.screen_color)

pygame.quit()
