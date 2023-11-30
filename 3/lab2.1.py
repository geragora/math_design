import turtle

# Функция для вычисления следующей точки на кривой Коха
def koch_curve(turtle, order, length):
    if order == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_curve(turtle, order - 1, length)
        turtle.left(60)
        koch_curve(turtle, order - 1, length)
        turtle.right(120)
        koch_curve(turtle, order - 1, length)
        turtle.left(60)
        koch_curve(turtle, order - 1, length)

# Запрашиваем у пользователя максимальное количество итераций
max_iterations = int(input("Enter the maximum number of iterations: "))

# Создаем окно и черепашку
window = turtle.Screen()
window.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()

# Рисуем кривую Коха
koch_curve(t, max_iterations, 400)

# Закрываем окно по клику
window.exitonclick()
