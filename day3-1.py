__author__ = 'Sergio'
file = open("input3.txt", "r")  # r-> read   w+->write
lines = file.readlines()
# print(len(lines))
file.close()

i = 0
m = len(lines)
id_square = [0]*m
corner_x = [0]*m
corner_y = [0]*m
width = [0]*m
height = [0]*m
#n = 1000
#fabric = [[0]*n]*n
n, m = 1000, 1000
fabric = [[0 for x in range(n)] for y in range(m)]

mayor_x = 0
mayor_y = 0

cont3 = 0
for line in lines:
    # line = lines[0]
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
    '''last_x = corner_x[i]+width[i]
    last_y = corner_y[i]+height[i]
    if last_x > mayor_x:
        mayor_x = last_x
    if last_y > mayor_y:
        mayor_y = last_y'''

    # print(list(range(1, 1+4)))

    '''if 394 <= i <= 394:
        print("#%s @ %d,%d: %dx%d" % (id_square[i], corner_x[i], corner_y[i], width[i], height[i]))'''

    for j in range(corner_x[i], corner_x[i]+width[i]):
        for k in range(corner_y[i], corner_y[i]+height[i]):
            fabric[j][k] += 1
            # print("en [%d,%d]" % (j, k))
            cont3 += 1
            '''if fabric[j][k] > 1:
                print("en [%d,%d]" % (j, k))'''
    i += 1

print(cont3)
i = 0
cont = 0
# cont2 = 0
for i in range(1000):
    # s = str(i)+"-> "
    for j in range(1000):
        # s += str(fabric[i][j])
        # s += " "
        if fabric[i][j] > 1:
            cont += 1
        # cont2 += 1
            # print("encontrada "+str(cont))
    # print(s)
print(cont)
# print(cont2)

# print("%d y %d" % (mayor_x, mayor_y))
'''
print(line[hash+1:arroba-1])
print(line[arroba+2:comma])
print(line[comma+1:twopoints])
print(line[twopoints+2:ex])
print(line[ex+1:])
'''

