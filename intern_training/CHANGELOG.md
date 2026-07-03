# Curriculum Changelog

## Recent Updates (July 2026)

### Program-Wide Consistency Pass
- **Fixed 29 broken `DAILY_TEMPLATE.md` links** across every day file (wrong relative path)
- **Week 2 weekend**: replaced a stray Django Task Tracker assignment with a Python package capstone (Django doesn't start until Week 5); fixed Deliverables for Days 2-5 to match actual daily content
- **Week 6**: Day 5 overview now matches the actual "Frontend Integration & Polish" lesson (was describing deployment prep instead); Day 4 dropped the untaught "Query Optimization" option, DRF is now the sole core path; added the missing `week06/weekend.md` (previously the only week without one)
- **Week 1 Day 3 / overview**: corrected the "JSON/CSV" claim to CSV-only (JSON is taught in Week 2)
- **Problem banks**: `ProblemBank_Django.md` grew from 22 to 34 problems with new Authentication & Permissions and REST API (DRF) sections, since Week 6 assigned problems from sections that didn't exist; all weekly problem-count quotas were reconciled against actual bank sizes (previously several weeks required solving more problems than their bank contained)
- **Week 3 (DSA)**: removed three problems cited in day files that don't exist in the bank; fixed Core/Stretch/Challenge tier mismatches between the overview and day files; reconciled per-day quotas with each bank section's actual size
- **Week 4**: removed a JavaScript/frontend requirement from Day 4 that depended on web material never taught in the program; aligned the weekend CLI spec (subcommands/flags) with what Day 3 actually teaches
- **Week 5**: added `priority` and `updated_at` to the Day 1 Task model spec (previously required by the weekend project but never taught); fixed a custom-manager naming mismatch and several Core/Stretch tier swaps
- **Coverage threshold**: standardized on `>85%` everywhere (previously varied between 80/85/90/95% across files with no stated reason)
- **Removed dead references** to `modules/` and `legacy/` (both non-existent in the current repo)

## October 2025

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

