import random
import numpy
import cv2

random.seed()
maze=[]
maxpix=255
minumpyix=0
size=10 # size -  размер. количество клеток лабиринта по высоте и ширине. лабиринт всегда квадратный
list=[minumpyix, maxpix]
dots=[]

def line():
    return minumpyix

def cell(j):
    if j%2==0:
        x=minumpyix
    else:
        x=maxpix
    return x

def scan(x,y):
    direction = ['up', 'down', 'left', 'right']
    ret=[x,y]
    for i in range (4):
        r=random.choice(direction)
        if (r == 'up'):
            try:
                if maze[x-2][y]==maxpix:
                    maze[x][y]=127
                    maze[x-2][y] = 127
                    maze[x - 1][y] = 127
                    ret[0]-=2
                    dots.append([x,y])
                    break
            except:
                r
        elif (r == 'down'):
            try:
                if maze[x + 2][y]==maxpix:
                    maze[x][y]=127
                    maze[x + 2][y]=127
                    maze[x + 1][y] = 127
                    ret[0]+=2
                    dots.append([x, y])
                    break
            except:
                r
        elif (r == 'left'):
            try:
                if maze[x][y-2]==maxpix:
                    maze[x][y] = 127
                    maze[x][y-2] = 127
                    maze[x][y - 1] = 127
                    ret[1] -= 2
                    dots.append([x, y])
                    break
            except:
                r
        elif (r == 'right'):
            try:
                if maze[x][y+2]==maxpix:
                    maze[x][y] = 127
                    maze[x][y+2] = 127
                    maze[x][y + 1] = 127
                    ret[1] += 2
                    dots.append([x, y])
                    break
            except:
                r

        direction.remove(r)
    return ret

def search(x,y):
    ret=[x,y]
    if maze2[x-1][y]==maxpix:
                    maze2[x][y]=127
                    maze2[x - 1][y] = 127
                    ret[0]-=1
                    dots.append([x,y])

    elif maze2[x + 1][y]==maxpix:
                    maze2[x][y]=127
                    maze2[x + 1][y] = 127
                    ret[0]+=1
                    dots.append([x, y])
    elif maze2[x][y-1]==maxpix:
                    maze2[x][y] = 127
                    maze2[x][y - 1] = 127
                    ret[1] -= 1
                    dots.append([x, y])
    elif maze2[x][y+1]==maxpix:
                    maze2[x][y] = 127
                    maze2[x][y + 1] = 127
                    ret[1] += 1
                    dots.append([x, y])
    return ret

for i in range(size):
    if i%2==0:
        maze.append([line() for j in range(size)])
    else:
        maze.append([cell(j) for j in range(size)])

x=1
y=1
maze[x][y]=127

while 1:
    ret = scan(x, y)
    if(x == ret[0] and y == ret[1]):
        back=dots.pop()
        ret=scan(back[0], back[1])
        x = ret[0]
        y = ret[1]
    else:
        x=ret[0]
        y=ret[1]
    if len(dots)==0:
        break

maze[size-2][size-1]=255
for x in range(size):
    for y in range(size):
        if maze[x][y]==127:
            maze[x][y]=255
dsize = (700, 700) #меняет размер окна с лабиринтом
maze2=maze
maze=cv2.resize((numpy.asarray(maze, numpy.uint8)), dsize, interpolation = cv2.INTER_AREA)
cv2.imshow("maze", numpy.asarray(maze, numpy.uint8))
cv2.waitKey(0)