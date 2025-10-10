## Week 4 · Day 1 — pytest Mastery

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A comprehensive pytest test suite with fixtures, parametrization, mocking, and property-based testing for all Week 1-2 code.

**Why does this matter for Django?**  
Django projects rely heavily on testing. Mastering pytest fixtures, mocking, and parametrization is essential for building maintainable Django test suites that catch bugs before production.

**What does success look like?**  
- Test suite with >90% coverage
- Fixtures reducing test code duplication
- Mocked external dependencies (no real file/network I/O in tests)

---

### Objectives
- Master pytest fixtures, parametrization, and mocking
- Learn property-based testing with hypothesis
- Build comprehensive test suites with >90% coverage

### Tasks
1) pytest Fundamentals Review
   - Test discovery and naming conventions
   - Assertions and assertion introspection
   - Test organization: conftest.py, test structure

2) Fixtures Deep Dive
   - Fixture scopes: function, class, module, session
   - Fixture parametrization
   - Fixture factories and autouse
   - setUp/tearDown with yield fixtures

3) Parametrized Tests
   - @pytest.mark.parametrize for multiple test cases
   - Combining fixtures and parametrize
   - Test IDs for readable output

4) Mocking and Patching
   - unittest.mock basics
   - Mocking external dependencies (API calls, file I/O)
   - patch decorator and context manager
   - Asserting mock calls

5) Property-Based Testing
   - Introduction to hypothesis library
   - @given decorator with strategies
   - Testing invariants and properties
   - Example: test string normalization is idempotent

6) Hands-on
   - Refactor Week 1-2 code with comprehensive pytest suite
   - Add fixtures for test data (CSV files, sample objects)
   - Parametrize edge cases
   - Mock file I/O operations
   - Solve 3-4 testing problems from ProblemBank_DataHandling.md

7) Problem solving
   - Core: Fixture factory pattern
   - Stretch: Property-based tests for data transforms
   - Parametrize CSV validation tests

### Outcomes
- Write clean, maintainable tests
- Use fixtures effectively
- Mock external dependencies properly
- Understand property-based testing

### Deliverables
- Comprehensive test suite for Week 1-2 code:
  - >90% coverage
  - Fixtures documented
  - Parametrized tests for edge cases
  - Mocked file/network operations
- Example property-based test
- `pytest.ini` configuration
- `Makefile` with `test`, `coverage` targets

### Submission checklist
- [ ] Test suite with >90% coverage
- [ ] Fixtures used appropriately
- [ ] At least 3 parametrized test functions
- [ ] At least 2 mocked dependencies
- [ ] Property-based test example
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


