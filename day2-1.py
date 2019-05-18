__author__ = 'Sergio'
file = open("input2.txt", "r")  # r-> read   w+->write
lines = file.readlines()
# print(len(lines))
file.close()


def containsxletters(palabra, n):
    #mayor = 0
    for letra in palabra:
        ans = 0
        for temp_letra in palabra:
            # i += 1
            if letra == temp_letra:
                ans += 1
        #if ans > mayor:
        #    mayor = ans
        if ans == n:
            return True
    #return mayor
    return False
c2 = 0
c3 = 0
for line in lines:
    if containsxletters(line, 2):
        c2 += 1
    if containsxletters(line, 3):
        c3 += 1
    #print(howmanyletters(line))

print(c2)
print(c3)
print((c2*c3))