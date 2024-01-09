def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (3 * number) + 1


value = int(input("Enter the integer number: \n"))

ans = value
while ans != 1:
    ans = collatz(ans)
    print(ans)
