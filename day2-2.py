__author__ = 'Sergio'
file = open("input2.txt", "r")  # r-> read   w+->write
lines = file.readlines()
# print(len(lines))
file.close()

total = 26

def differentchars(palabra1, palabra2):
    ans = 0
    for i in range(26):
        if palabra1[i] != palabra2[i]:
            ans += 1
    return ans

for i in range(len(lines)):
    menor = 10
    for j in range(i+1, len(lines)):
        n = differentchars(lines[i], lines[j])
        if n == 1:
            print("%s%s" % (lines[i], lines[j]))
        if n < menor:
            menor = n