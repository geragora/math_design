import turtle
import random

def draw_star(rays, length):
    if rays % 2 == 0 and rays != 6:
        angle = 180 - (360 / rays)
    else:
        angle = 180 - (180 / rays)
  
    turtle.color("black", random.choice(["red", "green", "blue", "yellow"]))
    turtle.begin_fill()
  
    for _ in range(rays):
        turtle.forward(length)
        turtle.right(angle)
    
    turtle.end_fill()

# Опции
num_rays = random.choice([5, 7, 9])
ray_length = random.randint(50, 200)

turtle.speed(2)  # Регулируйте скорость анимации

draw_star(num_rays, ray_length)

turtle.done()