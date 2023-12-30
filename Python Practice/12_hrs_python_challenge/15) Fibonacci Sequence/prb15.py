def fibonacci(n):
    i = 0
    j = 1
    lst = [i, j]

    for k in range(2, n):
        lst.append(lst[k - 1] + lst[k - 2])

    return lst


print(fibonacci(10))
