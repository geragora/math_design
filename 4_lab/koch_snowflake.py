import turtle

# Создание экрана
screen = turtle.Screen()
screen.title("Создание снежинок")
screen.bgcolor("black")

snowflake = turtle.Turtle()
snowflake.speed(0)  # Максимальная скорость

# Функция для рисования снежинки Коха
def generate_koch_snowflake(length, depth):
    if depth == 0:
        snowflake.forward(length)
        return
    else:
        length /= 3.0
        depth -= 1
        generate_koch_snowflake(length, depth)
        snowflake.left(60)
        generate_koch_snowflake(length, depth)
        snowflake.right(120)
        generate_koch_snowflake(length, depth)
        snowflake.left(60)
        generate_koch_snowflake(length, depth)

# Функция для рисования снежинки Коха с заданными параметрами
def draw_koch_snowflake(size, depth):
    snowflake.penup()
    snowflake.goto(-size/2, 0)  # Переместить черепашку в начальную позицию
    snowflake.pendown()
    snowflake.color("white")
    for _ in range(3):
        generate_koch_snowflake(size, depth)
        snowflake.right(120)

# Рисование снежинки Коха
draw_koch_snowflake(200, 4)

# Остановка программы при клике на экран
turtle.done()