def frequency_counter(lis):
    frequency = {}
    for l in lis:
        if l in frequency:
            frequency[l] += 1
        else:
            frequency[l] = 1
    return frequency


# print("Enter the list of numbers : ")
values = list(input("Enter the list of number without spaces: "))
print(frequency_counter(values))
