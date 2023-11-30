import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Углы для трех различных спиралей
angles = [0.1, 0.5, 1]
colors = ['b', 'g', 'r']

lines = [ax.plot([], [], color=c)[0] for c in colors] # lines to animate

# Настройка границ графика
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Инициализация линий
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Функция анимации
def animate(i):
    for angle, line in zip(angles, lines):
        t = np.linspace(0, i/10.0, 1000) # время
        x = t*np.cos(t+angle) # x координата
        y = t*np.sin(t+angle) # y координата

        line.set_data(x, y)
    return lines

# Создание анимации
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=500, interval=20, blit=True)

plt.show()