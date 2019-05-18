__author__ = 'Sergio'
file = open("input1.txt", "r")  # r-> read   w+->write
lines = file.readlines()
# print(len(lines))
s = 0
for line in lines:
    s += int(line)
    # print(line)
file.close()
print(s)
