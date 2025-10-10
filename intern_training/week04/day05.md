## Week 4 · Day 5 — Integration Testing & Performance

### Objectives
- Write integration tests for complete data pipelines
- Profile and optimize Python code
- Understand memory efficiency with generators

### Tasks
1) Integration Testing
   - Test full pipeline: Extract → Transform → Load
   - Temporary databases with SQLite in-memory
   - Temporary file fixtures with pytest tmp_path
   - Cleanup and teardown strategies

2) Test Database Setup
   - SQLite in-memory database for tests
   - Schema creation in fixtures
   - Test data seeding
   - Verify database state after pipeline

3) Performance Profiling
   - cProfile for function-level profiling
   - timeit for micro-benchmarks
   - Memory profiling with memory_profiler
   - Identify bottlenecks

4) Optimization Techniques
   - Generators for memory efficiency
   - List comprehensions vs. loops
   - Dict lookups vs. list searches
   - CSV processing with generators

5) Hands-on
   - Write integration tests for ETL pipeline
   - Test with temp database and files
   - Profile large file processing
   - Optimize using generators
   - Solve 2-3 integration testing problems

6) Problem solving
   - Core: Integration test for full pipeline
   - Stretch: Performance optimization (CSV processing)
   - Challenge: Memory-efficient processing with generators

### Outcomes
- Write meaningful integration tests
- Profile Python code effectively
- Optimize for performance and memory

### Deliverables
- Integration test suite (`test_integration.py`):
  - Full pipeline test with temp database
  - Fixtures for test data
  - Database state verification
  - File I/O with tmp_path
  - Tests pass with >90% coverage
- Performance report:
  - Profiling results (before/after)
  - Bottleneck identification
  - Optimization applied
  - Memory usage comparison
  - Benchmarks documented
- Optimized pipeline using generators

### Submission checklist
- [ ] Integration tests passing
- [ ] Temp database and files used correctly
- [ ] Performance profiling completed
- [ ] Optimization implemented with benchmarks
- [ ] Generators used for large data
- [ ] Test coverage >90%
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


