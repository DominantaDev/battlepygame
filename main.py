# Импорты
import pygame
import random

from entity import Entity
from projectile import Projectile

# Значения
WIDTH = 1000
HEIGHT = 800
CEIL = 10
FPS = 60

C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)
C_GREEN = (0, 255, 0)

# Настройки
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ZMEYAAAA')
clock = pygame.time.Clock()

Player = Entity(0, 0)

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
                Player.x -= 1
            elif event.key == pygame.K_d:
                Player.x += 1
            elif event.key == pygame.K_w:
                Player.y -= 1
            elif event.key == pygame.K_s:
                Player.y += 1
            
            # Стрельба
            if event.key == pygame.K_LEFT:
                Projectile(Player.x, Player.y, (-1, 0), 1/16)
            elif event.key == pygame.K_RIGHT:
                Projectile(Player.x, Player.y, (1, 0), 1/16)
            elif event.key == pygame.K_UP:
                Projectile(Player.x, Player.y, (0, -1), 1/16)
            elif event.key == pygame.K_DOWN:
                Projectile(Player.x, Player.y, (0, 1), 1/16)

    for pr in Projectile.ALL:
        pr.x += pr.impulse[0] * CEIL * pr.speed
        pr.y += pr.impulse[1] * CEIL * pr.speed

        pygame.draw.rect(screen, C_GREEN, (pr.x*CEIL, pr.y*CEIL, CEIL, CEIL))
        print(f"ID: {pr.id}, x: {pr.x}, y: {pr.y}")

    pygame.draw.rect(screen, C_RED, (Player.x*CEIL, Player.y*CEIL, CEIL, CEIL))
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(C_BLACK)

pygame.quit()