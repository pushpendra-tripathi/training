"""
practice module: string
"""

# 1. Write a function `is_palindrome(s: str) -> bool` that ignores case and spaces


def is_palindrome(s: str) -> bool:
    """
    function to check if a given string is pallindrome
    """
    return s.lower().strip().replace(" ", "")[::-1] == s.lower().strip().replace(
        " ", ""
    )


print(is_palindrome("abcba"))
print("\n")

# 2. Create `reverse_words(s: str) -> str` that reverses word order: "hello world" → "world hello"


def reverse_words(s: str) -> str:
    """
    function to return a reverse of a string
    """
    return " ".join(s.split()[::-1])


print(reverse_words("hello world"))


# 3. Implement `title_case(s: str) -> str` without using `.title()`: "hello world" → "Hello World"


def title_case(s: str) -> str:
    """
    function to implement title case without using inbuilf function
    """
    lst: list[str] = []
    for i in s.split():
        lst.append(i[0].upper() + i[1::])
    return " ".join(lst)


print(title_case("hello world"))
