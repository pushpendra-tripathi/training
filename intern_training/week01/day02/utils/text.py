"""
utility text.py

clean_text(): This is used to clean  a text in case of extra spaces, wrong cases,etc.

tokenize(): This is used to tokenize a string and store it in list

count_chars(): This returns a dictionary which contains the chars and their frequencies
                as key/values

"""


def clean_text(s: str) -> str:
    """
    - Input: raw string with extra spaces, mixed case, punctuation
    - Output: normalized lowercase string with single spaces and trimmed ends
    - Example: "  Hello,  WORLD!  " -> "hello, world!"
    """
    if len(s.split()) - 1 == s.count(" "):
        return s
    return clean_text(s.replace("  ", " ").lower().strip())
    # return s.lower().strip()


print(clean_text("  Hello,  WORLD!,               This      is     python"))
print("\n")


def tokenize(s: str = " ") -> list[str]:
    """
    - input: raw string
    - output: tokenized list containing the words of string
    - Example: "hello, world!" -> ["hello,", "world!"]
    """
    return s.split()


print(tokenize("  Hello,  WORLD!,               This      is     python"))
print("\n")


def count_chars(s: str) -> dict[str, int]:
    """
    - Input: string
    - Output: character frequency map
    - Example: "hello" -> {"h": 1, "e": 1, "l": 2, "o": 1}
    """

    return {
        i: clean_text(s).count(i)
        for i in clean_text(s)
        if i != " " and i != "," and i.isalnum()
    }


print(count_chars("  Hello,  WORLD!,               This      is     python"))
print("\n")
