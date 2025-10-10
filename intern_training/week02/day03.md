## Week 2 · Day 3 — Testing with pytest

### Objectives
- Set up pytest; write unit tests with fixtures and parametrization.

### Tasks
1) Setup
   - Install pytest and create `tests/` with an initial test file.
   - Configure `pytest.ini` and a `Makefile` target `test`.
2) Fixtures and parametrization
   - Write fixtures for small datasets and temp files.
   - Parametrize tests to cover edge cases for your I/O helpers.
3) Property-based testing (intro)
   - Add a small hypothesis-based test (optional) for a pure function.

### Expected Result
- Tests run and pass; failures provide clear diagnostics.
- All URLs use Django's URL namespacing and named patterns

### Problem solving (45–60 min)
- LeetCode: [Ransom Note](https://leetcode.com/problems/ransom-note/), [Plus One](https://leetcode.com/problems/plus-one/)

### Outcomes
- Confident test harness with meaningful coverage over utilities.

### Deliverables
- `tests/` directory with passing tests; `Makefile test` target.

### Submission checklist
- [ ] Tests cover happy/sad paths
- [ ] `make test` works on a clean clone
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


