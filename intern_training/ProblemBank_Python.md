## Problem Bank — Python Fundamentals (20+ problems)

**Target**: Week 1 and Week 2. Pick 5-7 problems daily; mix Core, Stretch, and Challenge.

### Core (must) — Strings & Lists

1) **Count vowels in a string**
   - Input: "hello world"
   - Output: 3
   - Edge cases: empty string, all consonants, all vowels

2) **Check if string is palindrome**
   - Input: "racecar"
   - Output: True
   - Input: "hello"
   - Output: False
   - Ignore: case, spaces, punctuation for stretch variant

3) **Find max in list**
   - Input: [3, 1, 4, 1, 5, 9]
   - Output: 9
   - Edge: empty list (raise error), single element

4) **Flatten nested list**
   - Input: [[1,2],[3,4],[5]]
   - Output: [1,2,3,4,5]

5) **Sum of even numbers**
   - Input: [1,2,3,4,5,6]
   - Output: 12

### Core (must) — Dictionaries & Sets

6) **Count word frequencies**
   - Input: "the quick brown fox jumps over the lazy dog"
   - Output: {"the": 2, "quick": 1, "brown": 1, ...}

7) **Merge two dictionaries**
   - Input: d1={"a":1,"b":2}, d2={"b":3,"c":4}
   - Output: {"a":1,"b":3,"c":4} (d2 values win)

8) **Find unique elements**
   - Input: [1,2,2,3,3,3,4]
   - Output: {1,2,3,4}

9) **Intersection of two lists**
   - Input: [1,2,3,4], [3,4,5,6]
   - Output: [3,4]

10) **Group items by length**
    - Input: ["a","bb","ccc","dd"]
    - Output: {1:["a"], 2:["bb","dd"], 3:["ccc"]}

### Stretch (nice) — Functions & Comprehensions

11) **FizzBuzz**
    - Input: n=15
    - Output: [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz"]

12) **List comprehension: squares of evens**
    - Input: [1,2,3,4,5,6]
    - Output: [4,16,36]

13) **Filter dict by value threshold**
    - Input: scores={"Alice":85,"Bob":92,"Charlie":78}, threshold=80
    - Output: {"Alice":85,"Bob":92}

14) **Nested comprehension: matrix transpose**
    - Input: [[1,2,3],[4,5,6]]
    - Output: [[1,4],[2,5],[3,6]]

15) **Prime number checker**
    - Input: 17
    - Output: True
    - Optimize: O(√n) vs O(n)

### Stretch (nice) — File I/O & Exceptions

16) **Read file and count lines**
    - Input: filepath="sample.txt"
    - Output: 42
    - Handle: FileNotFoundError with clear message

17) **Write list to CSV**
    - Input: data=[["Name","Age"],["Alice",30],["Bob",25]]
    - Output: CSV file with proper quoting
    - Use: csv module

18) **Parse JSON config file**
    - Input: config.json with {"api_key":"xxx","timeout":30}
    - Output: dict; raise ValueError if malformed

### Challenge (bonus)

19) **Implement zip() from scratch**
    - Input: [1,2,3], ['a','b','c']
    - Output: [(1,'a'),(2,'b'),(3,'c')]
    - Handle: unequal lengths

20) **Custom decorator: @timer**
    - Measure function execution time
    - Print: "function_name took 0.123 seconds"

21) **Context manager for file operations**
    - Implement `with FileHandler(path) as f:` that auto-closes
    - Handle: exceptions during processing

22) **Generator: fibonacci sequence**
    - Yield infinite fibonacci numbers
    - Memory: O(1)

23) **Recursive: calculate factorial**
    - Input: 5
    - Output: 120
    - Add: memoization for optimization

24) **Type hints: annotate a complex function**
    - Function signature with List[Dict[str,int]], Optional, Union
    - Use mypy to verify correctness

25) **Error handling: retry decorator**
    - Retry function up to n times on exception
    - Exponential backoff optional

### Guidance
- Write type hints for all functions
- Add docstrings with examples and complexity notes
- Test happy path + at least 2 edge cases per problem
- Use `pytest` and aim for >90% coverage
- Prefer pure functions (no side effects) where possible


