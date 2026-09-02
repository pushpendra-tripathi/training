"""
practice module: functions
"""

from statistics import mean, median


def greet(name: str, greeting: str = "Hello") -> str:
    """Return personalized greeting."""
    return f"Hello {name}, {greeting} from python"


print(greet("shiv", "good morning"))


def calculate_stats(*numbers: float) -> dict[str, float]:
    """Return min, max, mean, median of numbers."""
    return {
        "min": min(numbers),
        "max": max(numbers),
        "mean": mean(numbers),
        "median": median(numbers),
    }


def build_query(**params) -> str:
    """Build URL query string from keyword arguments."""
    querry: str = "?"
    for key, value in params.items():
        querry += f"{key}={value}"
        querry += "&"
    if querry[-1] == "&":
        querry = querry[: len(querry) - 2]
