__author__ = 'Sergio'
file = open("input3.txt", "r")  # r-> read   w+->write
lines = file.readlines()
file.close()

i = 0
m = len(lines)
id_square = [0]*m
corner_x = [0]*m
corner_y = [0]*m
width = [0]*m
height = [0]*m
n, m = 1000, 1000
fabric = [[0 for x in range(n)] for y in range(m)]

mayor_x = 0
mayor_y = 0

cont3 = 0
for line in lines:
    hash = line.find("#")
    arroba = line.find("@")
    comma = line.find(",")
    twopoints = line.find(":")
    ex = line.find("x")
    id_square[i] = line[hash+1:arroba-1]
    corner_x[i] = int(line[arroba+2:comma])
    corner_y[i] = int(line[comma+1:twopoints])
    width[i] = int(line[twopoints+2:ex])
    height[i] = int(line[ex+1:])
    for j in range(corner_x[i], corner_x[i]+width[i]):
        for k in range(corner_y[i], corner_y[i]+height[i]):
            fabric[j][k] += 1
            cont3 += 1
    i += 1

print(cont3)
i = 0
cont = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] > 1:
            cont += 1
print(cont)


i = 0
for line in lines:
    flag = True
    hash = line.find("#")
    arroba = line.find("@")
    comma = line.find(",")
    twopoints = line.find(":")
    ex = line.find("x")
    id_square[i] = line[hash+1:arroba-1]
    corner_x[i] = int(line[arroba+2:comma])
    corner_y[i] = int(line[comma+1:twopoints])
    width[i] = int(line[twopoints+2:ex])
    height[i] = int(line[ex+1:])
    for j in range(corner_x[i], corner_x[i]+width[i]):
        for k in range(corner_y[i], corner_y[i]+height[i]):
            if fabric[j][k] > 1:
                flag = False
    if flag:
        print(line)
    i += 1
