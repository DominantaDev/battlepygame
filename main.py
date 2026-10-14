# Импорты
import pygame
import random
import math
import consts
import world

from entity import Entity
from projectile import Projectile
from enemy import Enemy
from vector2 import *
from enums import *

# Значения
WIDTH = 1000
HEIGHT = 800
CEIL = 10
FPS = 30

# Настройки
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ZMEYAAAA')
clock = pygame.time.Clock()

Player = Entity(VectorZero, 2)

# Основной цикл
run = True
world.dt = 0

while run:
    world.dt = clock.tick(FPS) / 1000
    # Обработка эвентов
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # # Ходьба
            # if event.key == pygame.K_a:
            #     Player.pos += VectorLeft * Player.speed
            # elif event.key == pygame.K_d:
            #     Player.pos += VectorRight * Player.speed
            # elif event.key == pygame.K_w:
            #     Player.pos += VectorUp * Player.speed
            # elif event.key == pygame.K_s:
            #     Player.pos += VectorDown * Player.speed

            if event.key == pygame.K_SPACE:
                Enemy(Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)), 10)
            
            # Стрельба
            if event.key == pygame.K_LEFT:
                Projectile(Player.pos, VectorLeft, 1/16)
            elif event.key == pygame.K_RIGHT:
                Projectile(Player.pos, VectorRight, 1/16)
            elif event.key == pygame.K_UP:
                Projectile(Player.pos, VectorUp, 1/16)
            elif event.key == pygame.K_DOWN:
                Projectile(Player.pos, VectorDown, 1/16)
    
    for pr in Projectile.ALL:
        pr.pos += pr.impulse * world.dt

    for ent in Entity.ALL:
        # _action = ent.action_update(pygame.time.get_ticks())
        # if _action == Action.WALK:
        #     ent.Walk(dt)
        # elif _action == Action.CHASE:
        #     ent.Chase(dt)
        # elif _action == Action.SHOOT:
        #     ent.Shoot(dt)
        # elif _action == Action.MOVE:
        #     ent.Move(dt)
        ent.action_update(pygame.time.get_ticks())

        pygame.draw.rect(screen, ent.color, (ent.pos.x, ent.pos.y, CEIL, CEIL))
    
    # Cycle-end
    pygame.display.update()
    screen.fill(consts.BLACK)

pygame.quit()