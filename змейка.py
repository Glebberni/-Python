import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen_width = 800
screen_height = 600
cell_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змейка")

# Цвета
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Позиция и скорость змейки
snake = [(screen_width // 2, screen_height // 2)]
snake_speed = 1
snake_direction = (1, 0)

# Позиция еды
food = (random.randint(0, screen_width // cell_size - 1) * cell_size, random.randint(0, screen_height // cell_size - 1) * cell_size)

# Функция отрисовки змейки и еды
def draw():
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))
    pygame.display.flip()

# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    if keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)

    # Движение змейки
    x, y = snake[0]
    x += snake_direction[0] * cell_size
    y += snake_direction[1] * cell_size

    # Проверка столкновения с границами экрана
    if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
        pygame.quit()
        sys.exit()

    # Проверка на поедание еды
    if (x, y) == food:
        snake.append((x, y))
        food = (random.randint(0, screen_width // cell_size - 1) * cell_size, random.randint(0, screen_height // cell_size - 1) * cell_size)
    else:
        snake = [(x, y)] + snake[:-1]

    # Проверка на самопересечение
    if len(snake) != len(set(snake)):
        pygame.quit()
        sys.exit()

    # Отрисовка и обновление экрана
    draw()
    clock.tick(10)