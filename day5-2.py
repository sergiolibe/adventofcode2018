__author__ = 'Sergio'

from random import randint


def leer():
    file = open("input5.txt", "r")  # r-> read   w+->write
    line = file.readlines()
    line = list(line[0])
    file.close()
    line.pop(line.index('\n'))
    return line


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


def borrarTodasInstancias(cadena,indexletter):
    char=diccionarioLower()[indexletter]
    while char in cadena:
        cadena.pop(cadena.index(char))
    char=diccionarioUpper()[indexletter]
    while char in cadena:
        cadena.pop(cadena.index(char))


line=leer()
for x in range(0,26):
    line=leer()
    borrarTodasInstancias(line,x)
    a=buscaPar(line,0)
    # print(a)
    while a>-1:
        borraPar(line,a)
        a=buscaPar(line,a-3)
        # if (len(line))%10000==0:
        #     print(len(line))
    print(x,' (',diccionarioUpper()[x],')','=>',len(line))

# line=line[0:40]
# print(line)
# borrarTodasInstancias(line, 2)
# print(line)
# print(list(diccionarioLower()).index('h'))
# print(list(diccionarioLower()).index('z'))