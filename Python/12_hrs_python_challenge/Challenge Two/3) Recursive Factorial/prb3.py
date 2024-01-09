def factorial(n):
    if n < 1:
        return 1

    c = n - 1
    return n * factorial(c)


print(factorial(7))
