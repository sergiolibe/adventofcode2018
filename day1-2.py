__author__ = 'Sergio'
file = open("input1.txt", "r")  # r-> read   w+->write
lines = file.readlines()
# print(len(lines))
s = 0
i = 0
j = 0
s_partial = [1e6]


def busca_repetido(valor, vector):
    ans = False
    i = 0
    for x in vector:
        i += 1
        if valor == x:
            ans = True
            print(i)
    return ans

for vuelta in range(140):
    j += 1
    for line in lines:
        i += 1
        # print(line)
        s += int(line)
        # if i < 1000 or i > 140000:
            # print(str(s)+"  ["+str(i)+"]")
        # if busca_repetido(s, s_partial):
        #    print("....."+str(s)+"  ["+str(i)+"] vuelta "+str(vuelta))
        #    break
        s_partial.append(s)
        # print(len(s_partial))
file.close()
# print(s)

print("busco")
i = 0
menor = 200000
for s in s_partial:
    if s_partial.count(s) > 1:
        # print("find "+str(s)+" 2º->["+str(i)+"]")
        ocurrencias = [index for index, e in enumerate(s_partial) if e == s]
        # print("1º->["+str(s_partial.index(s))+"]")
        # print(ocurrencias)
        if ocurrencias[1] < menor:
            solucion = [i, s, ocurrencias]
            menor = ocurrencias[1]
        # break
    i += 1
    if i > 4200:
        break
print("i->"+str(solucion[0])+" valor->"+str(solucion[1])+" 1º->"+str(solucion[2][0])+" 2º->"+str(solucion[2][1]))