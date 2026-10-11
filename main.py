# Импорты
import pygame
import random
import math

from entity import Entity
from projectile import Projectile
from enemy import Enemy
from vector2 import Vector2

# Значения
WIDTH = 1000
HEIGHT = 800
CEIL = 10
FPS = 30

C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)
C_GREEN = (0, 255, 0)
C_BLUE = (0, 0, 255)

# Настройки
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ZMEYAAAA')
clock = pygame.time.Clock()

Player = Entity(Vector2(0, 0), 2)

# Основной цикл
run = True
while run:
    # Обработка эвентов
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # Ходьба
            if event.key == pygame.K_a:
                Player.pos += Vector2(-1, 0) * Player.speed
            elif event.key == pygame.K_d:
                Player.pos += Vector2(1, 0) * Player.speed
            elif event.key == pygame.K_w:
                Player.pos += Vector2(0, -1) * Player.speed
            elif event.key == pygame.K_s:
                Player.pos += Vector2(0, 1) * Player.speed

            if event.key == pygame.K_SPACE:
                Enemy(Vector2(random.randint(0, WIDTH)/CEIL, random.randint(0, HEIGHT))/CEIL, 1)
            
            # Стрельба
            if event.key == pygame.K_LEFT:
                Projectile(Player.pos, Vector2(-1, 0), 1/16)
            elif event.key == pygame.K_RIGHT:
                Projectile(Player.pos, Vector2(1, 0), 1/16)
            elif event.key == pygame.K_UP:
                Projectile(Player.pos, Vector2(0, -1), 1/16)
            elif event.key == pygame.K_DOWN:
                Projectile(Player.pos, Vector2(0, 1), 1/16)

    for enm in Enemy.ALL:
        enm_player = Vector2(Player.pos.x - enm.pos.x, Player.pos.y - enm.pos.y)
        enm.pos += enm_player.norm() * enm.speed

        pygame.draw.rect(screen, C_BLUE, (enm.pos.x*CEIL, enm.pos.y*CEIL, CEIL, CEIL))
        print(f"ID: {enm.id}, x: {enm.pos.x}, y: {enm.pos.y}")
    
    for pr in Projectile.ALL:
        pr.pos += pr.impulse * CEIL * pr.speed

        pygame.draw.rect(screen, C_GREEN, (pr.pos.x*CEIL, pr.pos.y*CEIL, CEIL, CEIL))
        # print(f"ID: {pr.id}, x: {pr.x}, y: {pr.y}")

    pygame.draw.rect(screen, C_RED, (Player.pos.x*CEIL, Player.pos.y*CEIL, CEIL, CEIL))
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(C_BLACK)

pygame.quit()