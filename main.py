# Импорты
import pygame

from entity import Entity

# Значения
WIDTH = 1000
HEIGHT = 800
CEIL = 10
FPS = 30

# Настройки
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Player = Entity(0, 0)

# Основной цикл
run = True
while run:
    # Обработка эвентов
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()