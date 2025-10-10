## Week 2 · Day 5 — Refactor and Test Hard Cases

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A refactored, clean codebase with comprehensive tests covering edge cases, boundary values, and error conditions.

**Why does this matter for Django?**  
Django applications grow complex quickly. Learning to refactor for clarity and write tests for edge cases prevents bugs in production and makes code maintainable.

**What does success look like?**  
- Code with early returns, extracted functions, and clear naming
- Tests covering malformed inputs and boundary values
- CI-ready test suite that passes on clean clone

---

### Objectives
- Refactor for clarity/performance; add tests for edge cases and error paths.

### Tasks
1) Refactoring
   - Apply early returns, extract small functions, and improve naming.
2) Tests
   - Add tests for malformed inputs, boundary values, and error handling.
3) CI-like run
   - Add `make test` and ensure clean runs from a fresh clone.

### Problem solving
- LeetCode: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/), [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### Outcomes
- Cleaner code with stronger tests and confidence in edge cases.

### Deliverables
- Tests passing; README notes on refactors and tricky cases.

### Submission checklist
- [ ] Tests cover edge and error cases
- [ ] `make test` works
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


