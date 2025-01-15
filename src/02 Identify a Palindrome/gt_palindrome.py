def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join([c for c in s if c.isalnum()])
    return s == s[::-1]

print(is_palindrome("Hello World!"))  # False
print(is_palindrome("Go hang a salami, I’m a lasagna hog."))
