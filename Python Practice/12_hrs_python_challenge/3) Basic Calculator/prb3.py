def calculator(n1, n2, op):

    if op == '+':
        value = n1 + n2
    elif op == '-':
        value = n1 - n2
    elif op == '-':
        value = n1 * n2
    elif op == '/':
        value = n1 / n2
    else:
        return -1
    return value


num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
operator = str(input("Enter the operator: "))
print("\nIf it returns -1 then you have entered invalid operator\n")

print(calculator(num1, num2, operator))
