## Week 4 — Testing + Data Engineering

### Weekly learning goals
- Master pytest: fixtures, parametrization, mocking, property-based testing
- Build robust data validation and ETL pipelines
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

#### Day 2 (Tue): Data Validation & ETL Pipelines
- Topics
  - Schema validation for CSV/JSON
  - Error collection (don't fail on first error)
  - Data transformation patterns
  - Pipeline design: Extract → Transform → Load
- Hands-on
  - Build validation module with clear error messages
  - Implement ETL pipeline for energy data
  - Solve 3-4 data handling problems from ProblemBank_DataHandling.md
- Problem solving
  - Core: CSV validation, JSON schema validation
  - Stretch: ETL Pipeline with error handling
  - Challenge: Data deduplication with fuzzy matching
- Deliverables
  - Validation module with tests; ETL pipeline working with comprehensive error handling

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

#### Day 5 (Fri): Integration Testing & Performance
- Topics
  - Integration tests for full pipelines
  - Temporary databases and file fixtures
  - Performance profiling basics
  - Memory efficiency with generators
- Hands-on
  - Write integration tests for ETL pipeline
  - Profile and optimize large file processing
  - Solve 2-3 integration testing problems
- Problem solving
  - Integration test: full pipeline
  - Performance: optimize CSV processing
- Deliverables
  - Integration test suite; performance benchmarks documented

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


