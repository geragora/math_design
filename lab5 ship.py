import numpy
import matplotlib.pyplot as pyplot
from celluloid import Camera

fig = pyplot.figure()
fig.set_figwidth(10)
fig.set_figheight(2)
camera = Camera(fig)

def res(n):
    trig = numpy.matrix([[numpy.cos(a), -numpy.sin(a)], [numpy.sin(a), numpy.cos(a)]])
    ship = numpy.matrix([[x[n]], [y[n]]])
    a1a2 = numpy.matrix([[xn], [numpy.sin(xn)]])
    xr = numpy.dot(trig, ship)+a1a2
    xi[n]=xr[0,0]
    yi[n]=xr[1,0]

x=[-1,-1,1,1]
y=[0,1,1,0]
xi=[0,0,0,0]
yi=[0,0,0,0]
xn=0

for i in range(125):
    a = numpy.arctan(numpy.cos(xn))
    for i in range(4):
        res(i)
    xn+=0.2
    pyplot.plot(xi, yi, 'r')
    pyplot.fill(xi,yi, 'r')
    camera.snap()

animation = camera.animate()
animation.save('animation.gif', writer='pillow')

x = numpy.linspace(-1, 25, 200)
pyplot.plot(x, numpy.sin(x))

pyplot.show()