import pygame
from pygame.draw import *

# Инициализация библиотеки pygame
pygame.init()

# Создание окна:
screen = pygame.display.set_mode((300, 200))

# Здесь рисуются фигуры
# ...

# Чтобы они отобразились на экране, его нужно обновить:
pygame.display.update()
# Эту же команду нужно повторять, если на экране происходят изменения

# нужно создать основной цикл, в котором будут отслеживаться
# происходящие события
# пока единственное интересующее событие - выход из программы

# Добавление небольшой задержки в главный цикл программы:
clock = pygame.time.Clock()
# 30 - максимальный FPS, быстрее которого программа работать не будет

while True:
    clock.tick(30)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()

