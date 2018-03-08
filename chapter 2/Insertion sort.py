# -*- coding: utf-8 -*-：

'''increasing order'''
def insertion_sort(x):
    if type(x) == int:              #如果输入是数字，则转为列表
        x = list(str(x))

    for j in range(1,len(x)):
        key = x[j]
        i = j - 1
        temp = ['']
        while i >= 0 and x[i] > key: #如果降序，则将大于改为小于
            temp[0] = x[i+1]
            x[i+1] = x[i]
            x[i] = temp[0]
            i -= 1
    return x


print(insertion_sort([31,41,59,26,41,58]))
print(insertion_sort(123654))