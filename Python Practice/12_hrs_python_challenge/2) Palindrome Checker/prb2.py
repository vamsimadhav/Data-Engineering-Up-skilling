def reverse(z):
    s = ""
    for i in z:
        s = i + s
    return s


def is_palindrome(s):
    clean_str = s.replace(' ', '').lower()
    reverse_str = reverse(clean_str)

    return clean_str == reverse_str


string = str(input("Enter the string which you want to check palindrome: "))

print(is_palindrome(string))
