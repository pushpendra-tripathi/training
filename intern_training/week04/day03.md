## Week 4 · Day 3 — CLI Tools with argparse

### Objectives
- Build professional-grade CLI tools with argparse
- Implement subcommands, help text, and validation
- Add logging with verbosity levels

### Tasks
1) argparse Fundamentals
   - Positional vs. optional arguments
   - Argument types and validation
   - Help text and usage messages
   - Mutually exclusive groups

2) Subcommands
   - add_subparsers for command hierarchy
   - Example: `pipeline validate`, `pipeline transform`, `pipeline load`
   - Per-subcommand arguments and help

3) Exit Codes & Error Handling
   - Exit codes: 0 (success), 1 (error), 2 (usage error)
   - Graceful error handling with clear messages
   - argparse.ArgumentTypeError for custom validation

4) Logging
   - logging module configuration
   - Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
   - --verbose flag to control log level
   - Structured logging with context

5) Configuration Management
   - Config files (JSON, YAML, INI)
   - Environment variables
   - Command-line overrides
   - Precedence: CLI > ENV > CONFIG > DEFAULTS

6) Hands-on
   - Build professional CLI for ETL pipeline from Day 2
   - Subcommands: `validate`, `transform`, `load`, `report`
   - Add `--verbose`, `--config`, `--output` flags
   - Comprehensive help text
   - Solve 2-3 CLI problems from ProblemBank_DataHandling.md

7) Problem solving
   - Core: CLI summary tool
   - Stretch: Plugin interface for file formats
   - Challenge: Logging and verbosity control

### Outcomes
- Build CLIs with excellent UX
- Provide helpful error messages and help text
- Implement professional logging

### Deliverables
- CLI tool (`cli.py`) for ETL pipeline:
  - Subcommands: validate, transform, load, report
  - `--help` comprehensive and clear
  - `--verbose` for DEBUG logging
  - `--config` for config file
  - Exit codes appropriate
  - Colored output (optional, using `colorama`)
- README with usage examples
- Tests for CLI argument parsing

### Submission checklist
- [ ] CLI with subcommands working
- [ ] `--help` text clear and useful
- [ ] Logging with verbosity control
- [ ] Exit codes correct
- [ ] Error messages helpful
- [ ] 2+ CLI problems solved
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


