# Intern Training Structure Overview

> **Quick Links**: [Main README](../README.md) | [TRAINING.md](TRAINING.md) | This Structure Guide

This document provides a high-level overview of the 4-week (+bonus Week 5) Django intern training program.

## Weekly Structure

Each week follows a consistent pattern:
- **Days 1–5**: Daily lessons with topics, hands-on tasks, problem-solving (45–60 min), and deliverables
- **Weekend**: Consolidation assignment with step-by-step tasks and **acceptance criteria** (promotion gate)

## Weekly Themes

### Week 1: Foundations
- **Focus**: Linux, Git, Python fundamentals (deep dive), shell scripting, DSA warmup
- **Python Topics**: Data structures (strings, lists, dicts, sets), functions (args/kwargs, scope/LEGB, type hints), control flow (comprehensions, exceptions, context managers)
- **Milestone**: CSV analytics CLI packaged as a module
- **Gate**: Code passes `black`, `isort`, `pylint`; CLI works correctly; understands Python fundamentals
- **Practice**: `day02_exercises.md` (optional but recommended)

### Week 2: Django Basics
- **Focus**: OOP fundamentals (from scratch), web basics (HTML/CSS/JS), Django project setup, CRUD, admin, templates
- **OOP Topics**: Basic classes, dunder methods, encapsulation (`@property`), inheritance vs composition, dataclasses
- **Milestone**: Django Task Tracker with CRUD and admin
- **Gate**: Search/filter/pagination working; seed data provided; admin has custom action; **OOP exercises completed**
- **Practice**: `day01_exercises.md` (mandatory for promotion)

### Week 3: Auth & APIs
- **Focus**: Authentication, forms/validation, simple REST API (DRF), testing basics
- **Milestone**: Authenticated Task Tracker with DRF API
- **Gate**: Filtering works; tests cover happy/sad paths; API documented

### Week 4: Templates & Polish
- **Focus**: Template consolidation, CRUD polish, testing basics
- **Milestone**: Template-driven UI polished; admin productive
- **Gate**: Templates DRY; list supports pagination/search/sorting; admin has custom action; tests pass

### Week 5 (Bonus): Fullstack
- **Prerequisite**: Must pass Week 4 gate
- **Focus**: Frontend (HTML/CSS/JS) consuming Django API
- **Milestone**: Fullstack demo with frontend client
- **Optional**: Only for interns who pass Week 4 and want to explore fullstack

## Learning Progression

```
Week 1: Python fundamentals (deep dive) + Linux + Git
   ↓ Gate: Python mastery (data structures, functions, control flow)
Week 2: OOP (classes → inheritance → dataclasses) + Django basics
   ↓ Gate: OOP exercises + Django CRUD working
Week 3: Auth + DRF APIs + Testing
   ↓ Gate: Authenticated API with tests
Week 4: Template-driven polish + Admin
   ↓ Gate: Production-ready templates + admin
Week 5 (optional): Fullstack integration
```

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
- `data/sample_logs/`: Shell scripting exercises (Week 1 Day 1)
- `data/energy/hourly_prices.csv`: CSV analysis tasks (Week 1 Day 3, Weekend)
- `data/web/energy_stats.json`: Web basics exercise (Week 2 Day 2)
- `frontend_template/`: Scaffold for Week 5 frontend

### Practice Exercises
- `week01/day02_exercises.md`: Python fundamentals (20+ exercises) - **Optional**
- `week02/day01_exercises.md`: OOP fundamentals (6 progressive exercises) - **Mandatory for Week 2 gate**

## Support Materials

- Weekly overviews: `week01.md` through `week05.md`
- Daily plans: `weekXX/dayYY.md`
- Weekend assignments: `weekXX/weekend.md`
- Main repo modules: Optional references in `modules/*`
