import pygame
import math

# Установка размеров окна и цвета фона
WIDTH, HEIGHT = 800, 800
BACKGROUND_COLOR = (0, 0, 0)

# Инициализация Pygame и создание окна
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_tree(x1, y1, angle, depth):
    fork_angle = 20
    base_len = 10.0
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
        pygame.draw.line(win, (255,255,255), (x1, y1), (x2, y2), 2)
        pygame.display.flip()  # Обновление дисплея после каждого рисования линии
        pygame.time.delay(100)  # Задержка в миллисекундах
        draw_tree(x2, y2, angle - fork_angle, depth - 1)
        draw_tree(x2, y2, angle + fork_angle, depth - 1)

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        win.fill(BACKGROUND_COLOR)
        draw_tree(WIDTH // 2, HEIGHT * 3 // 4, -90, 9)
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
