# -*- coding: utf-8 -*-：

import random

'''increasing order'''
def insertion_sort(x):

    for j in range(1,len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and x[i] > key: #如果降序，则将大于改为小于
            x[i+1] = x[i]
            i -= 1
        x[i+1] = key
    return x


random_list = list(random.randint(1, 99) for i in range(10))

print('before sort:\n', random_list)
print('after sort:\n', insertion_sort(random_list))