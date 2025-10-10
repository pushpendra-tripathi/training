# Intern Training Structure Overview

> **Quick Links**: [Main README](../README.md) | [TRAINING.md](TRAINING.md) | This Structure Guide

This document provides a high-level overview of the 6-week fundamentals-first Django intern training program with 115 curated problems.

## Weekly Structure

Each week follows a consistent pattern:
- **Days 1–5**: Daily lessons with topics, hands-on tasks, **5-7 curated problems daily**, and deliverables
- **Weekend**: Consolidation project assignment with **acceptance criteria** (promotion gate)
- **Problem-solving quota**: 25-40 problems per week depending on difficulty

## Weekly Themes (6-Week Plan)

### Week 1: Systems + Python Basics
- **Focus**: Linux, Git, shell workflows; Python data types, control flow, functions, modules; tooling (`black`/`isort`/`pylint`, type hints)
- **Problems**: 25-35 from ProblemBank_Python.md (strings, lists, dicts, comprehensions, functions, file I/O)
- **Milestone**: Energy Insights CLI with clean I/O and typed functions
- **Gate**: Lint/format pass; 25+ problems solved with tests; CLI works on sample data; daily log

### Week 2: Python Advanced + OOP
- **Focus**: Classes, inheritance, composition, dataclasses, dunder methods; exceptions, file I/O, CSV/JSON; packaging; pytest basics
- **Problems**: 20-25 from ProblemBank_OOP.md (class design, inheritance, composition, design patterns)
- **Milestone**: Refactored package with OOP design and unit tests
- **Gate**: OOP exercises completed; 20+ problems solved; tests cover happy/sad paths; pytest passes

### Week 3: Data Structures & Algorithms
- **Focus**: Arrays, hashmaps, stacks, queues; sorting, searching; two pointers, sliding window; **recursion & tree basics**; graph introduction; time/space complexity
- **Problems**: 30-40 from ProblemBank_DSA.md (35 total: arrays, stacks, queues, sorting, searching, patterns, **5 tree/recursion intro**, 2 graphs)
- **Milestone**: Algorithm implementations with tests and complexity analysis; understand recursion; DFS/BFS patterns
- **Gate**: 30+ DSA problems solved; complexity documented; pattern mastery demonstrated; recursive thinking comfortable
- **Note**: 21 advanced tree/graph problems available as optional bonus for interview prep

### Week 4: Testing + Data Engineering
- **Focus**: **Database fundamentals** (SQL, normalization, constraints, indexes, transactions); pytest mastery (fixtures, parametrization, mocking); data validation, ETL pipelines; CLI tools with argparse; HTTP/REST basics, Python `requests`
- **Problems**: 15-20 from ProblemBank_DataHandling.md (CSV/JSON processing, pipelines, validation, testing, database operations)
- **Milestone**: Complete data pipeline with comprehensive tests loading to SQLite with proper schema
- **Gate**: 15+ data problems solved; database schema with constraints; pipeline tested; HTTP/REST demo works

### Week 5: Django Foundations
- **Focus**: Project setup, apps, settings, migrations; models, ORM, QuerySets; URL routing, FBVs/CBVs, templates; forms, validation, CRUD; admin customization
- **Problems**: 15-20 from ProblemBank_Django.md (models, views, forms, templates, admin)
- **Milestone**: Task Tracker CRUD app with admin
- **Gate**: CRUD functional; forms validated; admin useful; 15+ Django problems solved; tests for models/views

### Week 6: Django Advanced + Integration
- **Focus**: Authentication, permissions, per-user data; form validation, messages; pagination, search, filtering; Django testing; DRF basics (optional)
- **Problems**: 10-15 from ProblemBank_Django.md (auth, API, testing, optimization)
- **Milestone**: Production-ready Django app with auth and tests
- **Gate**: Auth working; pagination/search implemented; comprehensive tests; 10+ advanced problems solved; deployment-ready

## Learning Progression (6-week fundamentals‑first)

```
Week 1: Systems + Python Basics (25-35 problems)
   ↓ Gate: CLI + 25+ problems + quality tools
Week 2: Python Advanced + OOP (20-25 problems)
   ↓ Gate: OOP package + 20+ problems + tests
Week 3: Data Structures & Algorithms (30-40 problems)
   ↓ Gate: 30+ DSA problems + complexity analysis
Week 4: Testing + Data Engineering (15-20 problems)
   ↓ Gate: ETL pipeline + 15+ problems + comprehensive tests
Week 5: Django Foundations (15-20 problems)
   ↓ Gate: CRUD app + 15+ Django problems + model/view tests
Week 6: Django Advanced + Integration (10-15 problems)
   ↓ Final: Production-ready app + auth + 10+ problems + deployment docs
```

**Total: 115-145 curated problems with tests and documentation from 115 available problems**

*Bonus: 21 advanced tree/graph problems available as optional interview prep (not counted in total)*

## Python & OOP Foundation (Core Focus)

The curriculum emphasizes Python and OOP mastery **before** Django:

### Week 1 - Python Deep Dive
- **Day 2**: Data structures (strings, lists, dicts, sets, tuples)
- **Day 2**: Functions (parameters, returns, scope/LEGB, type hints)
- **Day 3**: Control flow (conditionals, loops, comprehensions)
- **Day 3**: Exceptions and context managers
- **Day 4**: Modules and packaging
- **Day 5**: Refactoring and testing patterns

### Week 2 - OOP Mastery
- **Day 1**: Basic classes (`__init__`, methods, attributes)
- **Day 1**: Dunder methods (`__repr__`, `__str__`, `__eq__`)
- **Day 1**: Encapsulation (`@property`, private attributes)
- **Day 1**: Inheritance (base classes, `super()`, overriding)
- **Day 1**: Composition vs inheritance (when to use each)
- **Day 1**: Dataclasses (after understanding basics)

## Daily Workflow

1. **Morning**: Read day plan; review topics and function specs
2. **Mid-day**: Hands-on tasks with explicit input/output examples
3. **Afternoon**: Problem solving (LeetCode/Project Euler)
4. **Evening**: Submit PR with deliverables; run `black`, `isort`, `pylint`

## Weekend Workflow

1. **Saturday**: Complete step-by-step tasks
2. **Sunday**: Verify acceptance criteria; polish docs/screenshots
3. **Submit**: PR with weekend/ folder structure and README

## Promotion Gates

Each weekend assignment includes **acceptance criteria**. The invigilator reviews:
- ✅ All tasks completed as specified
- ✅ Code quality (formatting/linting pass)
- ✅ Documentation (README clear and complete)
- ✅ Screenshots/outputs demonstrate working features

**If all criteria met → Promote to next week**  
**If criteria not met → Repeat week or provide targeted support**

## Quality Standards

All Python code must pass:
- `black .` (formatting)
- `isort .` (import sorting)
- `pylint **/*.py` (linting)

Run before every submission.

## Resources Provided

### Data Files
- `data/sample_logs/`: Shell scripting exercises (Week 1)
- `data/energy/hourly_prices.csv`: CSV analysis tasks (Weeks 1–2)
- `data/web/energy_stats.json`: Web basics exercise (Week 3)
- `frontend_template/`: Optional scaffold (Week 5)

### Problem Banks (115 Curated Problems)
- `ProblemBank_Python.md`: 25 problems (Week 1-2) - Python fundamentals
- `ProblemBank_OOP.md`: 18 problems (Week 2) - OOP, design patterns
- `ProblemBank_DSA.md`: **35 problems** (Week 3) - Arrays, stacks, queues, sorting, searching, patterns, **5 tree/recursion intro**, 2 graphs
  - *Bonus: 21 advanced tree/graph problems for optional interview prep*
- `ProblemBank_DataHandling.md`: 15 problems (Week 4) - CSV/JSON, ETL, validation, testing
- `ProblemBank_Django.md`: 22 problems (Weeks 5-6) - Models, views, forms, templates, admin, DRF

### Legacy Files
- `legacy/ProblemBank_A.md`: **DEPRECATED** - Replaced by ProblemBank_Python.md and ProblemBank_DSA.md
- `legacy/ProblemBank_B.md`: **DEPRECATED** - Replaced by ProblemBank_OOP.md and ProblemBank_DataHandling.md
- `week01/day02_exercises.md`: Python fundamentals - **Optional supplement**
- `week02/day01_exercises.md`: OOP fundamentals - **Optional supplement**

## Support Materials

- Weekly overviews: `week01.md` through `week06.md`
- Daily plans: `weekXX/dayYY.md`
- Weekend assignments: `weekXX/weekend.md`
- Problem Banks: Curated problems with sample I/O and complexity guidance
- Main repo modules: Optional references in `modules/*`
