## Week 4 — Testing + Data Engineering

### Weekly learning goals
- **Understand database fundamentals**: SQL, normalization, constraints, indexes, transactions
- Master pytest: fixtures, parametrization, mocking, property-based testing
- Build robust data validation and ETL pipelines loading to databases
- Develop CLI tools with professional-grade UX
- Understand HTTP/REST and consume APIs with Python
- Apply TDD mindset to data processing workflows

### Daily schedule

#### Day 1 (Mon): pytest Mastery
- Topics
  - Fixtures: setup/teardown, scope, parametrization
  - Mocking and patching external dependencies
  - Property-based testing with hypothesis
  - Test organization and best practices
- Hands-on
  - Refactor Week 1-2 code with comprehensive pytest suite
  - Add fixtures for test data, parametrize edge cases
  - Solve 3-4 testing problems from ProblemBank_DataHandling.md
- Problem solving
  - Core: Fixture factory pattern, parametrize CSV validation
  - Stretch: Property-based tests for data transforms
- Deliverables
  - Comprehensive test suite with >90% coverage; fixtures documented

#### Day 2 (Tue): Database Fundamentals + Data Validation
- Topics
  - **SQL basics**: CREATE, INSERT, SELECT, UPDATE, DELETE, JOIN
  - **Database design**: Normalization (1NF, 2NF, 3NF), constraints (PK, FK, UNIQUE, NOT NULL)
  - **Indexes**: When and why to use them, performance impact
  - **Transactions**: ACID properties, BEGIN, COMMIT, ROLLBACK
  - **Python sqlite3**: Connections, cursors, parameterized queries (prevent SQL injection)
  - Schema validation for CSV/JSON
  - Data transformation patterns
  - Pipeline design: Extract → Transform → Load (to database)
- Hands-on
  - Create database schema with constraints and indexes
  - Implement CRUD operations with parameterized queries
  - Build validation module with clear error messages
  - Implement ETL pipeline loading to SQLite with transactions
  - Solve 3-4 data handling problems from ProblemBank_DataHandling.md
- Problem solving
  - Core: Database schema with constraints, CSV validation, JSON schema validation
  - Stretch: ETL Pipeline loading to database with transactions
  - Challenge: Transaction rollback on validation errors
- Deliverables
  - Database schema with constraints and indexes; validation module with tests; ETL pipeline loading to SQLite

#### Day 3 (Wed): CLI Tools with argparse
- Topics
  - argparse: subcommands, argument types, help text
  - Exit codes and error handling
  - Logging with levels and verbosity flags
  - Configuration management (files, env vars)
- Hands-on
  - Build professional CLI for ETL pipeline
  - Add `--verbose`, `--config`, `--output` flags
  - Solve 2-3 CLI-focused problems
- Problem solving
  - Core: CLI summary tool
  - Stretch: Plugin interface for formats
  - Challenge: Logging and verbosity
- Deliverables
  - Polished CLI with helpful `--help`; comprehensive logging

#### Day 4 (Thu): HTTP/REST + Python requests
- Topics
  - HTTP methods, status codes, headers
  - REST API principles and design
  - Python `requests`: GET, POST, error handling, authentication
  - API testing and mocking
- Hands-on
  - Build script to consume public API (weather, GitHub, etc.)
  - Handle rate limiting, retries, timeouts
  - Create simple web page rendering JSON (from Week 2 materials)
- Problem solving
  - Consume API and transform data
  - Error handling for network issues
- Deliverables
  - API client with error handling; static page rendering API data

#### Day 5 (Fri): Performance Optimization & Code Quality
- Topics
  - Performance profiling: cProfile, timeit, memory profiling
  - Optimization techniques: generators, better data structures, built-ins
  - Code quality: type hints, docstrings, unit testing review
  - Production-ready code checklist
- Hands-on
  - Profile ETL pipeline to find bottlenecks
  - Optimize using generators and better data structures
  - Ensure comprehensive unit test coverage (>85%)
  - Solve 2-3 optimization problems
- Problem solving
  - Core: Profile and optimize CSV processing
  - Stretch: Memory-efficient generators
  - Challenge: Optimize validation logic
- Deliverables
  - Performance report with benchmarks; optimized pipeline; unit tests >85% coverage

### Weekend assignment
**Complete Data Engineering Pipeline**

Build a production-grade ETL pipeline:

1. **Extract**: Read from multiple sources (CSV, JSON, API)
2. **Transform**: 
   - Validate with comprehensive schema checks
   - Clean and normalize data
   - Enrich with derived fields
   - Handle missing/malformed data gracefully
3. **Load**: Write to JSON and SQLite database
4. **CLI**: Professional interface with:
   - Subcommands: `validate`, `transform`, `load`, `report`
   - Helpful `--help` and error messages
   - Logging with `--verbose` flag
   - Configuration file support
5. **Testing**:
   - Unit tests for each transform
   - Integration tests for full pipeline
   - Property-based tests where applicable
   - >90% coverage
6. **Documentation**:
   - Comprehensive README
   - Architecture diagram
   - Example runs with output
   - Error handling guide

**Acceptance criteria:**
- Pipeline processes real data correctly
- 15+ data handling problems solved from ProblemBank
- Comprehensive test suite (unit + integration)
- CLI is professional and user-friendly
- Error handling is robust and informative
- Documentation is clear and complete
- Code quality tools pass

### Suggested problems (15-20 total for the week)
- See `intern_training/ProblemBank_DataHandling.md` (Core/Stretch/Challenge)
- Daily quota: 3-5 problems (focus on quality and testing depth)

### Promotion gate (advance to Week 5 if all met)
- ETL pipeline functional and tested
- 15+ data handling problems solved
- Test coverage >90%
- HTTP/REST concepts demonstrated
- CLI tools professional-grade
- Weekend assignment complete with all criteria
- Quality gates pass


