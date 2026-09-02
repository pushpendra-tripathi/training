from typing import Callable


def power(n: int) -> int:
    return n**2


def apply_to_values(d: dict[str, int], func: Callable[[int], int]) -> dict[str, int]:
    """Apply function to all dict values."""
    for key, value in d.items():
        d[key] = func(value)
    return d


def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """Divide a by b, return default if b is 0."""
    if b == 0:
        return default
    else:
        return a / b


def chain_functions(*funcs: Callable) -> Callable:
    """Return a function that applies all funcs in sequence."""
    # Example: chain_functions(str.strip, str.lower, str.title)
    def pipeline(value):
        result = value
        for f in funcs:
            result = f(result)
        return result
    return pipeline

