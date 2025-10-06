## Week 1 · Day 5 — DSA Warmup + Refactor and Test

### Objectives
- Strengthen algorithmic thinking; write tests for utilities; refactor for clarity.

### Prerequisites
- Week 1 codebase built; local black/isort/pylint available.

### Tasks
1) Write comprehensive tests
   - Add tests using `unittest` or `pytest` for all utility functions and key CLI functions.
   - **Test coverage should include**:
     - Happy paths: functions work correctly with valid inputs
     - Edge cases: empty strings, empty lists, None values
     - Error handling: invalid file paths, missing columns, malformed data
     - Boundary conditions: single items, very long strings, special characters
   - Write descriptive test names that explain what is being tested
   - Aim for at least 80% code coverage of your utility functions
   - Run tests with `python -m pytest` or `python -m unittest discover`

2) Refactor for clarity
   - Review your codebase and identify areas that could be improved:
     - Are function names clear and descriptive?
     - Are there repeated code blocks that could be extracted into functions?
     - Are there magic numbers that should be named constants?
     - Do functions have a single, clear responsibility?
     - Are edge cases handled early with guard clauses?
   - Apply refactoring techniques:
     - Extract functions for repeated logic
     - Rename variables and functions for clarity
     - Use early returns to reduce nesting
     - Break long functions into smaller, focused ones
   - **Important**: Ensure all tests pass after each refactoring step (behavior unchanged)

### Problem solving (45–60 min)
- LeetCode: [Binary Search](https://leetcode.com/problems/binary-search/), [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### Outcomes
- A small but well-tested codebase with readable functions and helpful names.

### Deliverables
- Test suite in `tests/` with clear naming and coverage of core logic.
- Short notes in README on how to run tests.

### Submission checklist
- [ ] Tests pass locally
- [ ] Refactor did not change behavior (unless intended and documented)
- [ ] Formatting/linting clean


