import turtle
import math

# Функция для вычисления следующей точки фрактала Дракон Хартера-Хейтуэя
def dragon_curve(order, length, angle, directions=None):
    if directions is None:
        directions = [1, 0]
    if order == 0:
        return directions

    new_directions = []
    for direction in directions:
        if direction == 1:
            new_directions.append(1)
        elif direction == 0:
            new_directions.append(0)

    new_directions.append(1)
    for direction in reversed(directions):
        if direction == 1:
            new_directions.append(0)
        elif direction == 0:
            new_directions.append(1)

    return dragon_curve(order - 1, length, angle, new_directions)

# Функция для рисования фрактала с помощью turtle
def draw_dragon_curve(order, length, angle, colors):
    directions = dragon_curve(order, length, angle)
    for i, direction in enumerate(directions):
        color_index = i % len(colors)  # Выбираем цвет из списка colors
        turtle.pencolor(colors[color_index])
        if direction == 1:
            turtle.forward(length)
            turtle.right(angle)
        elif direction == 0:
            turtle.forward(length)
            turtle.left(angle)

# Параметры фрактала
iterations = 6 # Максимальное количество итераций
length = 5
angle = 90

# Цвета для каждого уровня фрактала
level_colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'cyan']

# Инициализация черепахи
turtle.speed(0)  # Наивысшая скорость отрисовки

# Определение размеров экрана
screen_width = turtle.window_width()
screen_height = turtle.window_height()

# Определение центральной позиции на экране
center_x = 0
center_y = 0

# Настройка начальной позиции черепахи в центре экрана
turtle.penup()
turtle.goto(center_x, center_y)
turtle.pendown()

# Нарисовать фрактал максимально допустимого порядка
colors = level_colors
draw_dragon_curve(iterations, length, angle, colors)

# Вывод надписи "Iterations" в верхнем левом углу
turtle.penup()
turtle.goto(-screen_width / 2 + 10, screen_height / 2 - 20)
turtle.pendown()
turtle.write(f'Iterations: {iterations}', align='left', font=('Arial', 12, 'normal'))

turtle.done()
