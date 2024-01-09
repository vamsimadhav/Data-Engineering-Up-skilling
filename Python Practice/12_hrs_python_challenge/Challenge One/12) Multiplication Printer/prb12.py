def till_num_table(num):
    for i in range(1, num + 1):
        tables(i, num)


def tables(val, num):
    for i in range(1, num + 1):
        sum = i * val
        print("" + str(val) + " * " + str(i) + " = " + str(sum))
    print("\n")


print(till_num_table(10))
