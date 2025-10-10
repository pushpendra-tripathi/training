# Curriculum Changelog

## Recent Updates (October 2025)

### Documentation Structure Improvements
- **Added navigation links** between README.md, TRAINING.md, and STRUCTURE.md
- Each document now has clear "Quick Links" at the top for easy navigation
- Clarified the purpose of each document:
  - `README.md`: Setup instructions, daily index, submission guidelines
  - `TRAINING.md`: High-level overview and ground rules
  - `STRUCTURE.md`: Program structure, gates, and learning progression

### Daily Assignment Clarity Improvements
- **Removed overly prescriptive solutions** from daily assignments
- Daily tasks now describe **what to build** (requirements) instead of **how to build it** (implementation)
- Maintains clear problem statements and expected outcomes
- Encourages independent problem-solving and research

**Examples of changes:**
- **Before**: Provided complete code for Django models, views, and templates
- **After**: Describes model fields, view requirements, and expected behavior

### Configuration Updates
- **Removed 100-character line length customization** for black formatter
- Now uses black's default **88 characters** (PEP8 standard)
- Updated all references in README.md and week01/day02.md
- Updated pylint configuration to match black's line length

### Pre-commit Hook References
- **Removed all references to pre-commit hooks** (9 files updated)
- Replaced with explicit quality tool commands:
  - `black .`, `isort .`, `pylint **/*.py`
- Maintains code quality standards without additional tooling complexity

### Weekend Assignment Enhancements
All weekend assignments now include:
- Clear problem statements with business context
- Explicit input/output specifications
- Expected features with examples
- User journey walkthroughs
- Comprehensive acceptance criteria

### Code Quality Standards
- All Python code must pass: `black .`, `isort .`, `pylint **/*.py`
- Standards are consistently applied across all weeks
- Tools are configured to work together (isort profile=black)

## Philosophy

The curriculum emphasizes:
1. **Learning by doing**: Clear requirements, not copy-paste solutions
2. **Independent problem-solving**: Interns research and implement solutions
3. **Real-world skills**: Working with documentation, debugging, iterating
4. **Quality standards**: Consistent code formatting and linting from day one

