__author__ = 'Sergio'

from random import randint

file = open("input5.txt", "r")  # r-> read   w+->write
lines = file.readlines()
file.close()

# line=lines[0]
# line=list(line)
line=list(lines[0])
print(line[436])
line.pop(line.index('\n'))
print(line[436])
def buscaPar(cadena,pivoteComienzo):
    if pivoteComienzo<0:
        pivoteComienzo=0 

    index1 = -1
    index2 = -1
    flag1 = False
    flag2 = False
    i = pivoteComienzo
    for eslabon in range(pivoteComienzo,len(cadena)):
        if cadena[eslabon].isupper():
            index1 = index2
            flag1 = flag2
            index2 = diccionarioUpper().index(cadena[eslabon])
            flag2 = True
            # print(i)
            if index1 == index2 and flag1 != flag2:
                return i
        else:
            index1 = index2
            flag1 = flag2
            index2 = diccionarioLower().index(cadena[eslabon])
            flag2 = False
            # print(i)
            if index1 == index2 and flag1 != flag2:
                return i
        i += 1
    return -1


def diccionarioLower():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def diccionarioUpper():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def borraPar(cadena,eslabon):
    cadena.pop(eslabon-1)
    cadena.pop(eslabon-1)
    return None

# a='a'
# print(a.isupper())
# print(a in diccionarioUpper())
# print(a in diccionarioLower())
# print(buscaPar(line))
# b=diccionarioLower()
# print(b)
# b.pop(4)
# print(b)

# word='dabAcCaCBAcCcaDA'
# word=list(word)
# print(word)
# line=word
a=buscaPar(line,0)
print(a,"s")
# line=line[0:500]
while a>-1:
    borraPar(line,a)
    a=buscaPar(line,a-3)
    if (len(line))%1000==0:
        print(len(line))
    
print(len(line))
# print('listo')
# print(line)
# print(word)



# line=line[0:40]
# a=buscaPar(line,0)
# print(a)
# while a>-1:
#     print(line)
#     borraPar(line,a)
#     a=buscaPar(line,a-3)
#     print(a)
# print(line)
