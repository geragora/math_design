import turtle
import random

# Создание экрана
screen = turtle.Screen()
screen.title("Создание снежинок")
screen.bgcolor("black")

snowflake = turtle.Turtle()
snowflake.speed(0)  # Максимальная скорость

# Функция для рисования одной линии снежинки с анимацией
def draw_line(length, depth, animation_speed):
    if depth == 0:
        for _ in range(int(length/animation_speed)):
            snowflake.forward(animation_speed)
    else:
        length /= 3.0
        depth -= 1
        draw_line(length, depth, animation_speed)
        snowflake.left(60)
        draw_line(length, depth, animation_speed)
        snowflake.right(120)
        draw_line(length, depth, animation_speed)
        snowflake.left(60)
        draw_line(length, depth, animation_speed)

# Функция для рисования снежинки с анимацией
def draw_snowflake(size, depth, color, animation_speed):
    snowflake.color(color)
    for _ in range(6):
        draw_line(size, depth, animation_speed)
        snowflake.right(60)

# Функция для создания случайной снежинки
def create_snowflake():
    size = random.randint(50, 200)
    depth = random.randint(0, 3)
    angle = random.randint(0, 360)
    color = random.choice(['white', 'red', 'cyan', 'green', 'yellow'])
    snowflake.penup()
    snowflake.goto(0, 0)
    snowflake.pendown()
    snowflake.setheading(angle)
    
    # Анимация рисования снежинки
    animation_speed = 0.1  # Скорость анимации, 1 - максимальная скорость
    draw_snowflake(size, depth, color, animation_speed)
    screen.update()  # Обновление экрана после завершения рисования снежинки

# Анимация создания снежинок
def animate_snowflakes():
    screen.tracer(0)  # Отключение автоматического обновления экрана
    snowflake.clear()  # Очистка черепашки перед каждой снежинкой
    for _ in range(10):  # Создание 10 снежинок
        create_snowflake()
    screen.update()  # Обновление экрана
    screen.ontimer(animate_snowflakes, 500)  # Запуск анимации через 500 миллисекунд

# Запуск анимации
animate_snowflakes()

# Остановка программы при клике на экран
turtle.done()