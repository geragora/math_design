import numpy as numpy
import matplotlib.pyplot as pyplot

num = 7

fig, ax = pyplot.subplots()
fig.set_figwidth(6)
fig.set_figheight(6)

def square():
    x = [0, 1, 1, 0]
    y = [0, 0, 1, 1]
    for i in range(num):
        for j in range(num):
            for n in range(4):
                x[n] += 1
            pyplot.plot(x, y)
            pyplot.fill(x, y)
        x = [0, 1, 1, 0]
        for i in range(4):
            y[i] += 1
    pyplot.show()

def triangle():
    x = [0, 1/2, 1]
    y = [0, numpy.sqrt(3)/2, 0]
    for i in range(num):
        pyplot.plot(x, y)
        pyplot.fill(x, y)
        for j in range(num):
            x.pop(0)
            y.pop(0)
            x.append(x[0]+1)
            y.append(y[0])
            pyplot.plot(x, y)
            pyplot.fill(x, y)
        x = [0+(i+1)*0.5, 1/2+(i+1)*0.5, 1+(i+1)*0.5]
        y = [0+(i+1)*numpy.sqrt(3)/2, numpy.sqrt(3)/2+(i+1)*numpy.sqrt(3)/2, 0+(i+1)*numpy.sqrt(3)/2]
    pyplot.show()

def hexagon():
    x = [0, 0, 1/2, 1, 1, 1/2]
    y = [numpy.sqrt(3)/2, 1/(2*numpy.sqrt(3)), 0, 1/(2*numpy.sqrt(3)), numpy.sqrt(3)/2, 2/numpy.sqrt(3)]
    for i in range(num):
        for j in range(num):
            for n in range(6):
                x[n] += 1
            pyplot.plot(x, y)
            pyplot.fill(x, y)
        x = [0, 0, 1/2, 1, 1, 1/2]
        for j in range(6):
            x[j]+=1/2*(i+1)
        y = [numpy.sqrt(3)/2, 1/(2*numpy.sqrt(3)), 0, 1/(2*numpy.sqrt(3)), numpy.sqrt(3)/2, 2/numpy.sqrt(3)]
        for j in range (6):
            y[j]+=(i + 1) * numpy.sqrt(3) / 2
    pyplot.show()

def rhombus():
    xl = [0, 0, 1/2, 1/2]
    yl = [numpy.sqrt(3)/2, 1/(2*numpy.sqrt(3)), 0, 1/numpy.sqrt(3)]
    xr=[1/2, 1/2, 1, 1]
    yr=[0, 1/numpy.sqrt(3), numpy.sqrt(3)/2, 1/(2*numpy.sqrt(3))]
    xu=[0, 1/2, 1, 1/2]
    yu=[numpy.sqrt(3)/2, 1/numpy.sqrt(3), numpy.sqrt(3)/2, 2/numpy.sqrt(3)]
    for i in range(num):
        for j in range(num):
            pyplot.plot(xl, yl, xr, yr, xu, yu)
            pyplot.fill(xl, yl, "r", xr, yr, "g", xu, yu, "b")
            for z in range(4):
                xl[z]+=1
                xr[z]+=1
                xu[z]+=1
        xl = [0, 0, 1 / 2, 1 / 2]
        yl = [numpy.sqrt(3) / 2, 1 / (2 * numpy.sqrt(3)), 0, 1 / numpy.sqrt(3)]
        xr = [1 / 2, 1 / 2, 1, 1]
        yr = [0, 1 / numpy.sqrt(3), numpy.sqrt(3) / 2, 1 / (2 * numpy.sqrt(3))]
        xu = [0, 1 / 2, 1, 1 / 2]
        yu = [numpy.sqrt(3) / 2, 1 / numpy.sqrt(3), numpy.sqrt(3) / 2, 2 / numpy.sqrt(3)]
        for j in range(4):
            xl[j] += 1 / 2 * (i + 1)
            xr[j] += 1 / 2 * (i + 1)
            xu[j] += 1 / 2 * (i + 1)
        for j in range(4):
            yl[j] += (i + 1) * numpy.sqrt(3) / 2
            yr[j] += (i + 1) * numpy.sqrt(3) / 2
            yu[j] += (i + 1) * numpy.sqrt(3) / 2
    pyplot.show()


print('Please, choose a figure:\n'
      '1.Square\n'
      '2.Triangle\n'
      '3.Hexagon\n'
      '4.Rhombus\n'
      'Write anything else to exit.')

while (True):
    choice = input()
    if choice == '1':
        square()
    elif choice == '2':
        triangle()
    elif choice == '3':
        hexagon()
    elif choice == '4':
        rhombus()
    else:
        quit()