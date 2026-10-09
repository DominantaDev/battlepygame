# Импорты
import pygame
import random

from entity import Entity

# Значения
WIDTH = 1000
HEIGHT = 800
CEIL = 10
FPS = 30

C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)

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
            elif event.key == pygame.K_a:
                Player.x -= 1
            elif event.key == pygame.K_d:
                Player.x += 1
            elif event.key == pygame.K_w:
                Player.y -= 1
            elif event.key == pygame.K_s:
                Player.y += 1
            # elif event.key == pygame.K_SPACE:
            #     Player.x = random.randint(0, (WIDTH+1)//CEIL)
            #     Player.y = random.randint(0, (HEIGHT+1)//CEIL)
    print(Player.x, Player.y)

    screen.fill(C_BLACK)
    pygame.draw.rect(screen, C_RED, (Player.x*CEIL, Player.y*CEIL, CEIL, CEIL))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()