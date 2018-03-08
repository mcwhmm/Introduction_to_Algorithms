# -*- coding: utf-8 -*-：

import random

def selectionSort(x):
    if type(x) == int:
        x = list(str(x))

    for n in range(len(x)-1):
        current_val = x[n]
        i = n
        min = n
        while i < len(x)-1:
            if x[min] > x[i + 1]:
                min = i + 1
            i += 1
        x[n] = x[min]
        x[min] = current_val
    return x

test_list = list(random.randint(1, 99) for i in range(10))
print('origion list: ',test_list)
print('sorted list:  ',selectionSort(test_list))
# print('sorted list:  ',selectionSort([8,10,6,2,7]))