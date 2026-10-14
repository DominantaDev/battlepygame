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
from player import Player
from moveable_object import MoveableObject

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

player = Player()

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
            #     player.pos += VectorLeft * player.speed
            # elif event.key == pygame.K_d:
            #     player.pos += VectorRight * player.speed
            # elif event.key == pygame.K_w:
            #     player.pos += VectorUp * player.speed
            # elif event.key == pygame.K_s:
            #     player.pos += VectorDown * player.speed

            if event.key == pygame.K_SPACE:
                Enemy(Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)), target=player)
            
            # Стрельба
            if event.key == pygame.K_LEFT:
                Projectile(player.pos, VectorLeft, 50)
            elif event.key == pygame.K_RIGHT:
                Projectile(player.pos, VectorRight, 50)
            elif event.key == pygame.K_UP:
                Projectile(player.pos, VectorUp, 50)
            elif event.key == pygame.K_DOWN:
                Projectile(player.pos, VectorDown, 50)
    
    for pr in Projectile.ALL:
        pr.pos += pr.impulse * world.dt * pr.speed
        pygame.draw.rect(screen, pr.color, (pr.pos.x, pr.pos.y, CEIL, CEIL))

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