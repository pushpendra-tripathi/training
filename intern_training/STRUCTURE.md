# Intern Training Structure Overview

> **Quick Links**: [Main README](../README.md) | [TRAINING.md](TRAINING.md) | This Structure Guide

This document provides a high-level overview of the 6-week fundamentals-first Django intern training program with 127 curated problems.

## Weekly Structure

Each week follows a consistent pattern:
- **Days 1–5**: Daily lessons with topics, hands-on tasks, curated problems (pace varies by week — see each week's Focus below), and deliverables
- **Weekend**: Consolidation project assignment with **acceptance criteria** (promotion gate)
- **Problem-solving quota**: 10-35 problems per week depending on difficulty and bank size

## Weekly Themes (6-Week Plan)

### Week 1: Systems + Python Basics
- **Focus**: Linux, Git, shell workflows; Python data types, control flow, functions, modules; tooling (`black`/`isort`/`pylint`, type hints)
- **Problems**: 20-25 from ProblemBank_Python.md (strings, lists, dicts, comprehensions, functions, file I/O)
- **Milestone**: Energy Insights CLI with clean I/O and typed functions
- **Gate**: Lint/format pass; 20+ problems solved with tests; CLI works on sample data; daily log

### Week 2: Python Advanced + OOP
- **Focus**: Classes, inheritance, composition, dataclasses, dunder methods; exceptions, file I/O, CSV/JSON; packaging; pytest basics
- **Problems**: 15-18 from ProblemBank_OOP.md (class design, inheritance, composition, design patterns)
- **Milestone**: Refactored package with OOP design and unit tests
- **Gate**: OOP exercises completed; 15+ problems solved; tests cover happy/sad paths; pytest passes

### Week 3: Data Structures & Algorithms
- **Focus**: Arrays, hashmaps, stacks, queues; sorting, searching; two pointers, sliding window; **recursion & tree basics**; graph introduction; time/space complexity
- **Problems**: 25-35 from ProblemBank_DSA.md (35 total: arrays, stacks, queues, sorting, searching, patterns, **5 tree/recursion intro**, 2 graphs)
- **Milestone**: Algorithm implementations with tests and complexity analysis; understand recursion; DFS/BFS patterns
- **Gate**: 25+ DSA problems solved; complexity documented; pattern mastery demonstrated; recursive thinking comfortable
- **Note**: 21 advanced tree/graph problems available as optional bonus for interview prep

### Week 4: Testing + Data Engineering
- **Focus**: **Database fundamentals** (SQL, normalization, constraints, indexes, transactions); pytest mastery (fixtures, parametrization, mocking); data validation, ETL pipelines; CLI tools with argparse; HTTP/REST basics, Python `requests`
- **Problems**: 12-15 from ProblemBank_DataHandling.md (CSV/JSON processing, pipelines, validation, testing, database operations)
- **Milestone**: Complete data pipeline with comprehensive tests loading to SQLite with proper schema
- **Gate**: 12+ data problems solved; database schema with constraints; pipeline tested; HTTP/REST demo works

### Week 5: Django Foundations
- **Focus**: Project setup, apps, settings, migrations; models, ORM, QuerySets; URL routing, FBVs/CBVs, templates; forms, validation, CRUD; admin customization
- **Problems**: 15-19 from ProblemBank_Django.md (models, views, forms, templates, admin)
- **Milestone**: Task Tracker CRUD app with admin
- **Gate**: CRUD functional; forms validated; admin useful; 15+ Django problems solved; tests for models/views

### Week 6: Django Advanced + Integration
- **Focus**: Authentication, permissions, per-user data; form validation, messages; pagination, search, filtering; DRF; frontend integration
- **Problems**: 10-14 from ProblemBank_Django.md (auth, API, testing)
- **Milestone**: Full-stack Django app with auth, REST API, frontend, and tests
- **Gate**: Auth working; pagination/search implemented; API + frontend integrated; comprehensive tests; 10+ advanced problems solved

## Learning Progression (6-week fundamentals‑first)

```
Week 1: Systems + Python Basics (20-25 problems)
   ↓ Gate: CLI + 20+ problems + quality tools
Week 2: Python Advanced + OOP (15-18 problems)
   ↓ Gate: OOP package + 15+ problems + tests
Week 3: Data Structures & Algorithms (25-35 problems)
   ↓ Gate: 25+ DSA problems + complexity analysis
Week 4: Testing + Data Engineering (12-15 problems)
   ↓ Gate: ETL pipeline + 12+ problems + comprehensive tests
Week 5: Django Foundations (15-19 problems)
   ↓ Gate: CRUD app + 15+ Django problems + model/view tests
Week 6: Django Advanced + Integration (10-14 problems)
   ↓ Final: Full-stack app (auth + API + frontend) + 10+ problems + docs
```

**Total: 97-126 curated problems with tests and documentation from 127 available problems**

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
- `data/web/energy_stats.json`: Optional sample JSON data — not required by any graded task; use as an offline alternative to a public API in Week 4 Day 4
- `frontend_template/`: Scaffold for the Week 6 Day 5 frontend

### Problem Banks (127 Curated Problems)
- `ProblemBank_Python.md`: 25 problems (Week 1-2) - Python fundamentals
- `ProblemBank_OOP.md`: 18 problems (Week 2) - OOP, design patterns
- `ProblemBank_DSA.md`: **35 problems** (Week 3) - Arrays, stacks, queues, sorting, searching, patterns, **5 tree/recursion intro**, 2 graphs
  - *Bonus: 21 advanced tree/graph problems for optional interview prep*
- `ProblemBank_DataHandling.md`: 15 problems (Week 4) - CSV/JSON, ETL, validation, testing
- `ProblemBank_Django.md`: 34 problems (Weeks 5-6) - Models, views, forms, templates, admin, auth, REST API (DRF), testing

### Supplemental Files
- `week01/day02_exercises.md`: Python fundamentals - **Optional supplement**
- `week02/day01_exercises.md`: OOP fundamentals - **Mandatory for Week 2 gate**

## Support Materials

- Weekly overviews: `week01.md` through `week06.md`
- Daily plans: `weekXX/dayYY.md`
- Weekend assignments: `weekXX/weekend.md`
- Problem Banks: Curated problems with sample I/O and complexity guidance
