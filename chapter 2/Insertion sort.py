def insertion_sort(x):
    x = list(str(x))

    for j in range(1,len(x)):
        key = x[j]
        i = j - 1
        temp = ['']
        while i >= 0 and x[i] > key:
            temp[0] = x[i+1]
            x[i+1] = x[i]
            x[i] = temp[0]
            i -= 1
    return x

print(insertion_sort(987654321))
