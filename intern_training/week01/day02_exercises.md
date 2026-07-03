# Week 1 Day 2 — Python Fundamentals Practice Exercises

## Data Structures Exercises

### Strings
1. Write a function `is_palindrome(s: str) -> bool` that ignores case and spaces
2. Create `reverse_words(s: str) -> str` that reverses word order: "hello world" → "world hello"
3. Implement `title_case(s: str) -> str` without using `.title()`: "hello world" → "Hello World"

### Lists
1. `merge_sorted(list1: list[int], list2: list[int]) -> list[int]` - merge two sorted lists
2. `chunk_list(items: list, size: int) -> list[list]` - split into chunks: `[1,2,3,4,5], 2` → `[[1,2],[3,4],[5]]`
3. `flatten(nested: list[list]) -> list` - flatten one level: `[[1,2],[3,4]]` → `[1,2,3,4]`

### Dictionaries
1. `invert_dict(d: dict[str, str]) -> dict[str, str]` - swap keys and values
2. `merge_dicts(*dicts: dict) -> dict` - merge multiple dicts (later values override)
3. `filter_dict(d: dict, predicate) -> dict` - keep only items where predicate(key, value) is True

### Sets
1. `common_elements(list1: list, list2: list) -> set` - intersection of two lists
2. `unique_chars(s: str) -> set[str]` - unique characters in a string
3. `is_subset(set1: set, set2: set) -> bool` - check if set1 ⊆ set2

## Functions Exercises

### Basic Functions
```python
def greet(name: str, greeting: str = "Hello") -> str:
    """Return personalized greeting."""
    pass

def calculate_stats(*numbers: float) -> dict[str, float]:
    """Return min, max, mean, median of numbers."""
    pass

def build_query(**params) -> str:
    """Build URL query string from keyword arguments."""
    # Example: build_query(page=1, limit=10) → "?page=1&limit=10"
    pass
```

### Scope Practice
```python
counter = 0

def increment():
    """What happens here? How to modify global counter?"""
    counter += 1  # Will this work?

def outer():
    x = "outer"
    def inner():
        x = "inner"
        return x
    return inner()  # What gets returned?
```

### Type Hints Practice
Add complete type hints to these functions:
```python
def process_data(data, transform=None, filter_fn=None):
    """Process list with optional transform and filter."""
    pass

def group_items(items, key_func):
    """Group items by key_func result."""
    pass
```

## Comprehensions Practice

1. **List comprehension**: squares of even numbers from 1-20
   ```python
   squares = [...]
   ```

2. **Dict comprehension**: character → ASCII code for "hello"
   ```python
   char_codes = {...}
   ```

3. **Set comprehension**: unique word lengths in a sentence
   ```python
   sentence = "the quick brown fox jumps"
   lengths = {...}
   ```

4. **Nested comprehension**: multiplication table (1-5)
   ```python
   table = [[...] for ...]
   ```

## Integration Exercise

Create `utils/advanced.py` with:

```python
from typing import Callable, Any

def apply_to_values(d: dict[str, int], func: Callable[[int], int]) -> dict[str, int]:
    """Apply function to all dict values."""
    pass

def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """Divide a by b, return default if b is 0."""
    pass

def chain_functions(*funcs: Callable) -> Callable:
    """Return a function that applies all funcs in sequence."""
    # Example: chain_functions(str.strip, str.lower, str.title)
    pass
```

## Testing Your Solutions

Create `tests/test_day02.py`:
```python
import unittest
from utils.text import clean_text, tokenize, count_chars
from utils.collections import frequencies, dedupe, group_by

class TestTextUtils(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("  HELLO  "), "hello")
    
    # Add more tests...

class TestCollections(unittest.TestCase):
    def test_frequencies(self):
        self.assertEqual(frequencies(["a", "b", "a"]), {"a": 2, "b": 1})
    
    # Add more tests...

if __name__ == "__main__":
    unittest.main()
```

## Success Criteria

- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] Tests pass: `python -m unittest tests.test_day02`
- [ ] Code passes: `black .`, `isort .`, `pylint **/*.py`
- [ ] Can explain scope (LEGB rule) with examples
- [ ] Can explain when to use list vs dict vs set
