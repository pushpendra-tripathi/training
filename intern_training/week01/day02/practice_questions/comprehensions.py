"""
practice module: comprehensions
"""

# list comprehension
squares = [i**2 for i in range(1, 5)]


# dictionary comprehension
char_codes = {i: ord(i) for i in ["a", "b", "c"]}


# set comprehension
sentence = "the quick brown fox jumps"
lengths = {len(i) for i in sentence}


# nested comprehension
table = [[i * j for j in range(1, 5)] for i in range(6, 10)]
