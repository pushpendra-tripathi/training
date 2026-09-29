"""
Person class
"""


class Person:
    """Represent a person with name and age."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Return introduction string."""
        return f"Hello, my name is {self.name} and I am {self.age} years old"

    def is_adult(self) -> bool:
        """Return True if age >= 18."""
        return self.age >= 18


if __name__ == "__main__":
    person = Person("Alice", 25)
    print(person.introduce())  # "Hi, I'm Alice and I'm 25 years old."
    print(person.is_adult())
