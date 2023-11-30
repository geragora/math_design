import turtle

# Функция для рисования треугольника Серпинского
def draw_sierpinski(turtle, order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        size /= 2.0
        draw_sierpinski(turtle, order - 1, size)
        turtle.forward(size)
        draw_sierpinski(turtle, order - 1, size)
        turtle.backward(size)
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        draw_sierpinski(turtle, order - 1, size)
        turtle.left(60)
        turtle.backward(size)
        turtle.right(60)
# Запрашиваем у пользователя максимальное количество итераций
max_iterations = int(input("Enter the maximum number of iterations: "))
# Создаем окно и черепашку
window = turtle.Screen()
window.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-100, -100)
t.pendown()


# Рисуем треугольник Серпинского
draw_sierpinski(t, max_iterations, 200)

# Закрываем окно по клику
window.exitonclick()
