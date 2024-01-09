def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
        i += 1

    return True


def find_primes(n):
    primes = []

    for i in range(0, n + 1):
        if is_prime(i):
            primes.append(i)

    return primes


value = int(input("Enter the number: "))
print(find_primes(value))
