import math as m
import random as r

ar4 = [12, 9, 14, 6]
ar5 = [12, 9, 14, 6, 15]
ar7 = [12, 9, 14, 6, 22, 8, 13]

num_of_ele = r.randint(2, 1000)

def randomArray():

    ar = []
    for x in range(1, num_of_ele):
        ar.append(r.randint(1, 1000))

    return splitArray(ar)


def splitArray(ar):
    if (len(ar) <= 1):
        return ar

    x = m.ceil(len(ar) / 2)

    left = splitArray(ar[:x])
    right = splitArray(ar[x:])

    # print(left)
    # print(right)

    return mergeArrays(left, right)

def mergeArrays(ar1, ar2):
    ar = []

    ar1.reverse()
    ar2.reverse()

    for item1 in ar1[::-1]:
        for item2 in ar2[::-1]:
            if item1 < item2:
                ar.append(ar1.pop())
                break
            else:
                ar.append(ar2.pop())

    if len(ar1) > 0:
        for item in ar1[::-1]: ar.append(item)
    if len(ar2) > 0:
        for item in ar2[::-1]: ar.append(item)

    return ar


print('\nNumber of elements sorted: ' + str(num_of_ele) + '\n')
print(randomArray())

#Got help from https://github.com/javedqadruddin/MergeSort/blob/master/mergeSort.py