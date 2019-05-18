__author__ = 'Sergio'

from random import randint

file = open("input4.txt", "r")  # r-> read   w+->write
lines = file.readlines()
file.close()


class Date:
    def __init__(self, year, month, day, h, m, msg):
        self.year = year
        self.month = month
        self.day = day
        self.h = h
        self.m = m
        self.msg = msg

    def __str__(self):
        return "["+str(self.year)+"-"+str(self.month)+"-"+str(self.day)+" "+str(self.h)+":"+str(self.m)+"] "+str(self.msg)

    def menorque(self, another):
        if self.year < another.year:
            return True
        else:
            if self.year > another.year:
                return False
            if self.year == another.year and self.month < another.month:
                return True
            else:
                if self.month > another.month:
                    return False
                if self.month == another.month and self.day < another.day:
                    return True
                else:
                    if self.day > another.day:
                        return False
                    if self.day == another.day and self.h < another.h:
                        return True
                    else:
                        if self.h > another.h:
                            return False
                        if self.h == another.h and self.m < another.m:
                            return True
                        else:
                            return False


class Guard:
    def __init__(self, id, m_asleep):
        self.id = id
        self.m_asleep = m_asleep


def find_guard(guards, id):
    i = 0
    for guard in guards:
        if guard.id == id:
            return i
        i += 1
    return -1


def quicksort(lst, start, end):
    if start < end:
        pivot = randint(start, end)
        # swap with the last element
        lst[end], lst[pivot] = lst[pivot], lst[end]
        split = partition(lst, start, end)
        # sort both halves
        quicksort(lst, start, split-1)
        quicksort(lst, split+1, end)

def partition(lst, start, end):
    pivot_index = start-1
    for index in range(start, end):
        # compare with pivot
        #if lst[index] < lst[end]:
        if lst[index].menorque(lst[end]):
            pivot_index += 1
            # swap
            lst[pivot_index], lst[index] = lst[index], lst[pivot_index]
    # swap with the last element
    lst[pivot_index+1], lst[end] = lst[end], lst[pivot_index+1]

    return pivot_index+1

nums = [7, 2, 5, 1, 29, 6, 4, 19, 11]
print(nums)
#quicksort(nums, 0, len(nums)-1)
print(nums)

d1 = Date(1518, 12, 13, 9, 34, "h1")
d2 = Date(1518, 12, 13, 8, 34, "h2")
d3 = Date(1518, 12, 12, 9, 34, "h3")
d4 = Date(1518, 12, 13, 9, 32, "h4")
dates = [d1, d2, d3, d4]
for date in dates:
    print(date)

quicksort(dates, 0, len(dates)-1)
print("sorted")

for date in dates:
    print(date)

records = []
for line in lines:
    records.append(Date(line[1:5], line[6:8], line[9:11], line[12:14], line[15:17], line[19:]))

quicksort(records, 0, len(records)-1)

id = 0
guards = []

for record in records:
    print(record)
    if "Guard" in record.msg:
        id = record.msg[7:11]
        if find_guard(guards, id) == -1:
            guards.append(Guard(id, 0))
            index_guard = find_guard(guards, id)
        else:
            index_guard = find_guard(guards, id)
    if "falls" in record.msg:
        m1 = record.m
    if "wakes" in record.msg:
        m2 = record.m
        guards[index_guard].m_asleep += (int(m2)-int(m1))
    # print(record.msg[7:11])
mayor = Guard(0, 0)
for guard in guards:
    if guard.m_asleep > mayor.m_asleep:
        mayor = guard
print(mayor.id)
print(mayor.m_asleep)
for guard in guards:
    print("#%s con %d" % (guard.id, guard.m_asleep))

flag = False
cont = []
for i in range(60):
    cont.append(0)

for record in records:
    if "Guard" in record.msg:
        if mayor.id in record.msg:
            flag = True
        else:
            flag = False

    if flag:
        if "falls" in record.msg:
            m1 = record.m
        if "wakes" in record.msg:
            m2 = record.m
            for i in range(int(m1), int(m2)):
                cont[i] += 1
j=0
mostcommon = 0
mostcommonid = 0
for i in cont:
    print("%d -> %d" % (j, i))
    if i > mostcommon:
        mostcommon = i
        mostcommonid = j
    j += 1
print(mostcommonid)
print(mostcommonid*int(mayor.id))

'''
print(lines[0][1:5])
print(lines[0][6:8])
print(lines[0][9:11])
print(lines[0][12:14])
print(lines[0][15:17])
print(lines[0][19:])
'''