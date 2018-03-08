import random


def selectionSort(x):

    if type(x) == int:
        x = list(str(x))


    for n in range(len(x)-1):
        i = n + 1
        while i < len(x):
            if x[i-1] >= x[i]:
                min_pos = i
            i += 1
        temp = x[n]
        x[n] = x[min_pos]
        x[min_pos] = temp
        print(x[n])

    return x


print(selectionSort(87654321))