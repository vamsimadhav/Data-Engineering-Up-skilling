def frequency_counter(lis):
    frequency = {}
    for l in lis:
        if l in frequency:
            frequency[l] += 1
        else:
            frequency[l] = 1
    return frequency


# values = list(input("Enter the list of number without spaces: "))
li = input("Enter the list of numbers separated by spaces : ")
string_list = li.split(' ')
values = [int(num) for num in string_list]  # List Comprehension in Python
print(frequency_counter(values))
