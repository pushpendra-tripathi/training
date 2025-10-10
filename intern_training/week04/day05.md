## Week 4 · Day 5 — Performance Optimization & Code Quality

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A performance-optimized ETL pipeline using profiling tools, generators, and better data structures, with documented before/after benchmarks.

**Why does this matter for Django?**  
Django apps handling large datasets need optimization. Understanding profiling, generators, and algorithmic efficiency helps you build Django views and querysets that scale.

**What does success look like?**  
- Identified bottleneck with profiling evidence
- Measurable performance improvement (documented with numbers)
- Code still maintains >85% unit test coverage

---

### Objectives
- Profile and optimize Python code for performance
- Understand memory efficiency with generators and iterators
- Apply best practices for production-ready code
- Master unit testing patterns

### Tasks
1) **Performance Profiling**
   - **cProfile**: Function-level profiling
     - Identify slow functions
     - Understand call counts and cumulative time
   - **timeit**: Micro-benchmarks for specific operations
   - **Memory profiling**: Track memory usage with simple techniques
   - **Identify bottlenecks**: Where is the code actually slow?

2) **Optimization Techniques**
   - **Generators for memory efficiency**:
     - When to use generators vs. lists
     - CSV processing with generators (streaming large files)
     - yield vs. return
   - **Data structure choice**:
     - Dict lookups O(1) vs. list searches O(n)
     - Set membership vs. list membership
   - **List comprehensions**:
     - Faster than explicit loops
     - When comprehensions hurt readability
   - **Built-in functions**:
     - map, filter, zip - when they're faster
     - any(), all() for short-circuit evaluation

3) **Practical Optimization Example**
   - Start with working code processing large CSV
   - Profile to find bottleneck
   - Optimize:
     - Replace list with generator
     - Use dict for lookups instead of linear search
     - Use built-ins where appropriate
   - Measure improvement (before/after benchmarks)

4) **Code Quality Checklist**
   - Type hints on all functions
   - Docstrings with complexity notes
   - Unit tests with >85% coverage
   - No code smells (long functions, deep nesting, magic numbers)
   - DRY principle applied
   - Error handling appropriate

5) **Unit Testing Review**
   - Review pytest patterns from Day 1
   - Ensure ETL pipeline has comprehensive unit tests:
     - Each extractor tested separately
     - Each transformer tested separately
     - Each loader tested separately
     - Edge cases covered
     - Error paths tested
   - Mocking external dependencies (files, network)
   - Fixtures for test data

6) **Hands-on**
   - Profile your ETL pipeline from earlier this week
   - Identify bottleneck (likely CSV processing or transformation)
   - Optimize using generators and better data structures
   - Document before/after performance with benchmarks
   - Ensure unit tests still pass and coverage >85%
   - Solve 2-3 optimization problems from ProblemBank_DataHandling.md

7) **Problem solving**
   - Core: Profile and optimize CSV processing
   - Stretch: Memory-efficient processing with generators
   - Challenge: Optimize validation logic with better data structures

### Outcomes
- Profile Python code to find bottlenecks
- Optimize code using appropriate techniques
- Understand memory vs. speed tradeoffs
- Write production-ready code with quality gates

### Deliverables
- **Performance report** (`PERFORMANCE.md`):
  - Profiling results (before optimization)
  - Bottleneck identification with evidence
  - Optimization applied (what and why)
  - Benchmarks (before/after with numbers)
  - Memory usage comparison
- **Optimized ETL pipeline**:
  - Uses generators for large file processing
  - Improved data structures where appropriate
  - Still passes all unit tests
  - Performance improvement documented
- **Unit test suite** (if not already >85%):
  - Coverage >85%
  - All components tested separately
  - Edge cases and error paths covered
  - Mocked external dependencies
- **Code quality**:
  - All functions have type hints
  - All functions have docstrings
  - No pylint warnings
  - Clean, readable code

### Submission checklist
- [ ] Performance profiling completed
- [ ] Bottleneck identified and documented
- [ ] Optimization implemented with benchmarks
- [ ] Generators used for large data processing
- [ ] Unit test coverage >85%
- [ ] All tests passing
- [ ] Performance report created
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them

### Notes
- **Focus on real bottlenecks**, not premature optimization
- **Measure before and after** - don't guess
- **Generators** are powerful for memory, but add complexity - use when needed
- **Unit tests > integration tests** for this program - keep tests simple and focused


