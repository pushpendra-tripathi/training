## Week 1 · Day 2 — Python Essentials I + Local Quality Tools

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A utility module with clean, typed, tested Python functions for text and collection manipulation, passing professional quality tools.

**Why does this matter for Django?**  
Django views process data (strings, lists, dicts). Clean Python with type hints and quality checks prevents bugs and makes code maintainable.

**What does success look like?**  
- Functions with type hints and docstrings that pass `black`, `isort`, `pylint`
- Can manipulate strings, lists, and dicts confidently
- Quality tools configured and running automatically

---

### Objectives
- Master core Python data types and functions.
- Set up and use `black`, `isort`, and `pylint` locally for code quality.

### Prerequisites
- Git repo cloned; virtualenv activated.

### Tasks
1) Python fundamentals (deep dive)
   - **Data structures practice**
     - Strings: slicing, f-strings, `str.join()`, `str.split()`, `str.strip()`
     - Lists: slicing, list comprehensions, `append()`, `extend()`, `sort()` vs `sorted()`
     - Tuples: unpacking, named tuples for simple structures
     - Dicts: iteration, `get()` with defaults, dict comprehensions
     - Sets: union, intersection, difference; when to use sets vs lists
   - **Functions deep dive**
     - Parameters: positional, keyword, default values, `*args`, `**kwargs`
     - Return values: single vs multiple (tuple unpacking)
     - Scope: local, enclosing, global, built-in (LEGB rule)
     - Type hints: basic syntax `def func(x: int) -> str:`
   - **Write `utils/text.py` with functions**
     - Function specs
       - `clean_text(s: str) -> str`
         - Input: raw string with extra spaces, mixed case, punctuation
         - Output: normalized lowercase string with single spaces and trimmed ends
         - Example: "  Hello,  WORLD!  " -> "hello, world!"
       - `tokenize(s: str, delimiter: str = " ") -> list[str]`
         - Input: text string, optional delimiter (default space)
         - Output: list of word tokens split on delimiter
         - Example: "hello, world!" -> ["hello,", "world!"]
       - `count_chars(s: str) -> dict[str, int]`
         - Input: string
         - Output: character frequency map
         - Example: "hello" -> {"h": 1, "e": 1, "l": 2, "o": 1}
   - **Write `utils/collections.py` with functions**
     - Function specs
       - `frequencies(items: list[str]) -> dict[str, int]`
         - Input: list of strings
         - Output: dict mapping item -> count
         - Example: ["a","b","a"] -> {"a": 2, "b": 1}
       - `dedupe(items: list[str]) -> list[str]`
         - Input: list with duplicates
         - Output: list preserving first occurrence order
         - Example: ["a","b","a"] -> ["a","b"]
       - `group_by(items: list[dict], key: str) -> dict[str, list[dict]]`
         - Input: list of dicts, key to group by
         - Output: dict mapping key values to lists of items
         - Example: `[{"status":"todo","id":1}, {"status":"done","id":2}]` grouped by "status"
2) Local quality tools
   - Install tools: `pip install black isort pylint`.
   - Configure:
     - `pyproject.toml` (black default settings per PEP8)
     - `.isort.cfg` (profile = black)
     - `.pylintrc` (ignore venv, follow black line-length)
3) First run
   - Run formatters/linters locally:
     - `black .`, `isort .`, and `pylint **/*.py` (use `|| true` if needed to see reports).

### Problem solving
- LeetCode: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/), [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### Outcomes
- Clean, consistent Python code and a working local quality pipeline.

### Deliverables
- Committed `utils/` module with docstrings and type hints.
- Config files for black, isort, pylint.
- Completed exercises from `day02_exercises.md` (optional but recommended).
- Short `README.md` section describing how to run formatting and lint locally.

### Submission checklist
- [ ] Ran `black .` and `isort .`, and addressed `pylint` feedback
- [ ] Functions have clear docstrings and type hints
- [ ] README updated with commands
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why quality tools matter for Django teams
  - [ ] Documented Python patterns learned (comprehensions, type hints, LEGB scope)


