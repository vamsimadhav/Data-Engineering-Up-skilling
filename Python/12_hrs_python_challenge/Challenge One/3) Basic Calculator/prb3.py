def calculator(n1, n2, op):
    # Forgot about / by 0 operation

    if op == '+':
        value = n1 + n2
    elif op == '-':
        value = n1 - n2
    elif op == '-':
        value = n1 * n2
    elif op == '/':
        value = n1 / n2 if n2 != 0 else -1
    else:
        return -1
    return value


num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
operator = str(input("Enter the operator: "))
print("\nIf it returns -1 then you have entered invalid operator\n")

print(calculator(num1, num2, operator))
