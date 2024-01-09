def reverse_string(z):
    """
    Complicated the solution too much
    lst = []
    for i in range(0, len(z)):
        lst.append(z[i])

    s = 0
    e = len(z) - 1
    while s <= e:
        lst[s], lst[e] = lst[e], lst[s]
        s += 1
        e -= 1

    return "".join(x for x in lst)
    """
    str = ""
    for char in z:
        str = char + str

    return str

print(reverse_string("Vamsi"))
