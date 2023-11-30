import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def julia_set(c, xlim, ylim, res, max_iter):
    x = np.linspace(xlim[0], xlim[1], res[0])
    y = np.linspace(ylim[0], ylim[1], res[1])
    X, Y = np.meshgrid(x, y)
    img = np.zeros(X.shape, dtype=float)
    Z = X + 1j * Y
    for i in range(max_iter):
        Z = Z**2 + c
        mask = np.abs(Z) < 1000
        img += mask
    img = np.log(img + 1)
    return img

def animate(i):
    ax.clear()
    img = julia_set(c=complex(0.7885*np.cos(i), 0.7885*np.sin(i)), xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), res=(500, 500), max_iter=256)
    ax.imshow(img, extent=(-1.5, 1.5, -1.5, 1.5))

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 100), interval=100)
plt.show()
