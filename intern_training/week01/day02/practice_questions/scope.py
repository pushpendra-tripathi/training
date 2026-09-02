"""
practice module: scope
"""

counter = 0


def increment():
    """What happens here? How to modify global counter?"""
    counter += 1  # Will this work?


# no, it will throw an error


def outer():
    x = "outer"

    def inner():
        x = "inner"
        return x

    return inner()  # What gets returned?


# inner
