## Week 2 · Weekend Assignment — Polished Python Package

### Objective
Consolidate OOP, error handling, file I/O, testing, and CLI ergonomics into a finished, installable Python package.

### Problem Statement
Finalize your "Energy Insights" package (started in Week 1, refactored during Week 2) into a production-quality Python package that:
- Loads hourly prices CSV/JSON data and computes daily averages, top-N spikes, and basic anomaly detection (z-score threshold is fine)
- Provides a robust CLI with subcommands, clear help text, validation, and useful exit codes
- Handles bad inputs gracefully (missing files, malformed rows, unknown columns) with clear error messages
- Ships with a solid pytest suite and a complete README

### Expected Features

#### 1. Package Structure
- **Layout**: `energy_insights/` with `__init__.py`, `__main__.py`, and modules with clear separation of concerns (I/O, transforms, CLI)
- **Public API**: a small, documented set of functions importable from the package root
- **Custom exceptions**: e.g. `DataLoadError`, `ValidationError` raised for bad inputs

#### 2. CLI
- **Entry point**: `python -m energy_insights`
- **Subcommands**: e.g. `summary`, `spikes`, `anomalies`
- **Arguments**: `--file <path>`, `--metric <column>`, `--top <n>`; validated with helpful messages
- **Exit codes**: 0 on success, non-zero on usage/data errors
- **Example**: `python -m energy_insights spikes --file data/hourly_prices.csv --metric price --top 5`

#### 3. Error Handling & I/O
- Context managers for all file access; `pathlib` throughout
- CSV and JSON readers with row validation and clear diagnostics (line numbers where practical)
- No unhandled tracebacks for user errors — catch, explain, exit non-zero

#### 4. Test Suite
- pytest with fixtures for sample datasets and temp files
- Parametrized tests covering edge cases (empty file, missing column, non-numeric values)
- Tests for error paths as well as happy paths
- `make test` runs the suite on a clean clone

#### 5. Documentation
- README with install/run instructions, CLI examples with sample output, and package overview
- Module docstrings describing each module's role

### Example CLI Flow
```
1. python -m energy_insights --help          → clear top-level help with subcommands
2. python -m energy_insights summary --file data/hourly_prices.csv
                                             → row count, min/max/mean per numeric column
3. python -m energy_insights spikes --file data/hourly_prices.csv --top 5
                                             → top 5 price spikes, pretty-printed
4. python -m energy_insights summary --file missing.csv
                                             → "Error: file not found: missing.csv", exit code 1
```

### Step-by-step tasks
1) Package polish
   - Finalize module boundaries and the public API; add `__repr__`/equality where classes are used.
2) CLI ergonomics
   - Add subcommands with argparse; write helpful `--help` text; validate arguments; return correct exit codes.
3) Error handling
   - Introduce custom exceptions; convert internal errors into clear user-facing messages.
4) Tests
   - Cover core logic, error paths, and boundary inputs; parametrize edge cases; add fixtures for temp files.
5) Docs
   - Update README with install/run examples and sample outputs.
6) Quality
   - Run `black .`, `isort .`, and `pylint **/*.py` locally; ensure `make format`, `make lint`, `make test` all work.

### Acceptance criteria (promotion to Week 3)
- CLI works end-to-end on sample data; invalid inputs produce clear messages and non-zero exit codes.
- Test suite passes and covers core logic, error paths, and edge cases.
- Package structure is clean with a documented public API.
- README is complete; formatting and linting pass locally.

### Submission checklist
- [ ] CLI subcommands + validation + exit codes working
- [ ] `make test` green on a clean clone; error paths covered
- [ ] README with examples and sample output
- [ ] Formatting/lint clean
