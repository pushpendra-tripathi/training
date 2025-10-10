## Week 4 · Weekend — Complete Data Engineering Pipeline

### Overview
Build a production-grade ETL pipeline with comprehensive testing, professional CLI, and complete documentation.

### Requirements

#### 1. Extract (Multiple Sources)
Implement data extraction from:
- **CSV files**: energy data, transactions, user data
- **JSON files**: configuration, nested API responses
- **Public API**: Real-time data (weather, GitHub, stock prices, etc.)

Each extractor should:
- Handle missing files/endpoints gracefully
- Validate source data format
- Return standardized internal format
- Log extraction progress

#### 2. Transform (Validate + Clean + Enrich)
Implement comprehensive data transformation:
- **Schema Validation**:
  - Required fields present
  - Correct data types
  - Value range checks
  - Custom business rules
  - Collect ALL errors (don't fail on first)
- **Data Cleaning**:
  - Strip whitespace
  - Normalize values (case, format)
  - Handle missing values (fill, drop, flag)
  - Remove duplicates
- **Data Enrichment**:
  - Derived fields (calculations, aggregations)
  - Lookups from reference data
  - Timestamp conversions
  - Data type conversions

#### 3. Load (Multiple Destinations)
Implement data loading to:
- **JSON file**: Validated and transformed data
- **SQLite database**: 
  - Proper schema with constraints
  - Indexes on frequently queried fields
  - Atomic transactions
  - Error rollback

#### 4. Professional CLI
Build CLI with subcommands:
```bash
# Validate source data
python -m pipeline validate --source data.csv --schema schema.json

# Transform data
python -m pipeline transform --input data.csv --output clean.json --config config.yaml

# Load to database
python -m pipeline load --input clean.json --db pipeline.db

# Full pipeline
python -m pipeline run --config config.yaml --verbose

# Generate report
python -m pipeline report --db pipeline.db --format table
```

Features required:
- **Subcommands**: validate, transform, load, run, report
- **Arguments**: `--source`, `--output`, `--config`, `--verbose`, `--dry-run`
- **Help text**: Comprehensive `--help` for each subcommand
- **Exit codes**: 0 (success), 1 (error), 2 (usage error)
- **Progress**: Show progress for long operations
- **Logging**: Configurable verbosity (INFO/DEBUG)
- **Configuration**: Support config files + env vars + CLI overrides

#### 5. Comprehensive Testing
Test suite must include:
- **Unit Tests** (>90% coverage):
  - Each extractor
  - Each validator
  - Each transformer
  - Each loader
  - CLI argument parsing
- **Comprehensive Unit Tests** (>90% coverage):
  - Each component tested separately
  - End-to-end test with temp database and files
  - Error scenarios covered
  - Rollback on database failure tested
- **Property-Based Tests** (at least 2):
  - Data transformations
  - Validation rules
- **Mocking**:
  - File I/O operations
  - API calls
  - Database connections
- **Fixtures**:
  - Test data (CSV, JSON)
  - Database schema
  - Config files

#### 6. Documentation
Create comprehensive documentation:
- **README.md**:
  - Project overview
  - Installation instructions
  - Quick start guide
  - Configuration options
  - Usage examples
  - Architecture diagram
- **ARCHITECTURE.md**:
  - System design
  - Data flow diagram
  - Component responsibilities
  - Error handling strategy
- **API.md** (if applicable):
  - Public API client usage
  - Rate limits
  - Authentication
- **TESTING.md**:
  - How to run tests
  - Test organization
  - Coverage requirements

### Suggested Structure
```
week04/
  weekend/
    README.md
    ARCHITECTURE.md
    pipeline/
      __init__.py
      cli.py                # CLI entry point
      extractors/
        __init__.py
        csv_extractor.py
        json_extractor.py
        api_extractor.py
      validators/
        __init__.py
        schema.py
        rules.py
      transformers/
        __init__.py
        cleaner.py
        enricher.py
      loaders/
        __init__.py
        json_loader.py
        db_loader.py
      config.py
      logger.py
    tests/
      conftest.py           # Shared fixtures
      test_extractors.py
      test_validators.py
      test_transformers.py
      test_loaders.py
      test_pipeline.py       # End-to-end pipeline test
      test_cli.py
      fixtures/             # Test data
        sample.csv
        sample.json
        schema.json
    schemas/
      energy_schema.json
      user_schema.json
    config/
      dev.yaml
      prod.yaml
    data/                   # Sample input data
      energy_prices.csv
      transactions.json
```

### Acceptance Criteria
- [ ] **Extract**: Read from CSV, JSON, and public API
- [ ] **Transform**: Schema validation + cleaning + enrichment
- [ ] **Load**: Write to JSON and SQLite with proper schema
- [ ] **CLI**: All subcommands working with helpful `--help`
- [ ] **Logging**: Configurable verbosity with structured logs
- [ ] **Configuration**: Config file + env vars + CLI overrides
- [ ] **Error Handling**:
  - [ ] Graceful error messages
  - [ ] Error collection (all errors, not just first)
  - [ ] Database rollback on failure
  - [ ] Retry logic for API calls
- [ ] **Testing**:
  - [ ] Test coverage >90%
  - [ ] Unit tests for all components
  - [ ] End-to-end pipeline test with temp database
  - [ ] Mocked external dependencies
  - [ ] Property-based tests (2+)
- [ ] **Documentation**:
  - [ ] README with setup and usage
  - [ ] Architecture diagram
  - [ ] Code comments and docstrings
  - [ ] Example runs with output
- [ ] **Code Quality**:
  - [ ] Passes `black`, `isort`, `pylint`
  - [ ] Type hints throughout
  - [ ] No security issues (secrets in env, not code)
- [ ] **Problem Solving**: 15+ problems from ProblemBank_DataHandling.md

### Promotion Gate
To advance to Week 5 (Django), you must:
- ✅ Meet all acceptance criteria above
- ✅ Pipeline processes real data end-to-end
- ✅ Tests pass with >90% coverage
- ✅ CLI is professional and user-friendly
- ✅ Documentation is comprehensive
- ✅ Code quality tools pass
- ✅ Demonstrate understanding of ETL principles

### Tips
- Start with a simple working pipeline, then add features
- Test as you build, don't save testing for last
- Use temp files/databases in tests for isolation
- Mock external APIs to make tests fast and reliable
- Profile before optimizing
- Clear error messages are as important as correct code
- Documentation should enable someone else to use your pipeline


