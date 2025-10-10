## Week 2 · Day 2 — Exceptions, Files, CSV/JSON

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A robust I/O utilities module with custom exceptions, context managers, and CSV/JSON processing with validation.

**Why does this matter for Django?**  
Django handles file uploads and data imports constantly. Understanding exception handling and file I/O is critical for building reliable data ingestion endpoints.

**What does success look like?**  
- Custom exceptions for clear error reporting
- Context managers for safe resource handling
- Validated CSV/JSON readers with proper error messages

---

### Objectives
- Handle errors gracefully using exceptions and context managers.
- Read/validate/write CSV and JSON reliably.

### Tasks
1) Exceptions and context managers
   - Create custom exceptions for invalid inputs.
   - Use `with` statements for files; ensure resources are closed and errors are surfaced clearly.
2) CSV/JSON processing
   - Add `io_utils.py` with helpers: `read_csv`, `read_json`, `write_csv`, `write_json`.
   - Validate inputs (required columns, types) and raise clear errors.
3) Integration
   - Extend your Energy Insights package to use these helpers, with typed signatures and docstrings.

### Problem solving
- Project Euler: [Problem 3](https://projecteuler.net/problem=3)
- LeetCode: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

### Outcomes
- Robust I/O layer with clear validation and error reporting.

### Deliverables
- `io_utils.py` with tests and usage examples.
- README notes on error behaviors and sample commands.

### Submission checklist
- [ ] Custom exceptions defined and used
- [ ] I/O helpers tested on happy/sad paths
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them

