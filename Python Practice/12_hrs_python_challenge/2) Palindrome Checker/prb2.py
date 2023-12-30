def reverse(z):
    s = ""
    for i in z:
        s = i + s
    return s


def is_palindrome(s):
    """
    Im using a reverse function here and using python methods

    clean_str = s.replace(' ', '').lower()
    reverse_str = reverse(clean_str)

    return clean_str == reverse_str
    """
    clean_str = "".join(e for e in s if e.isalnum()).lower()
    return clean_str == clean_str[::-1]


string = str(input("Enter the string which you want to check palindrome: "))

print(is_palindrome(string))
