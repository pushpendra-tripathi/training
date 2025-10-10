## Intern Training Program (6 Weeks: Fundamentals-First)

This folder contains a complete, self-contained Django intern training package with a strong fundamentals focus. It includes week-by-week lesson plans with daily tasks, comprehensive problem-solving practice (100+ curated problems), and weekend assignments with **promotion gates** at the end of each week.

### Quick Links
- **[PHILOSOPHY.md](intern_training/PHILOSOPHY.md)** - ⭐ **START HERE**: Training philosophy and first principles
- **[TRAINING.md](intern_training/TRAINING.md)** - High-level overview and ground rules
- **[STRUCTURE.md](intern_training/STRUCTURE.md)** - Program structure, gates, and learning progression
- **[DAILY_TEMPLATE.md](intern_training/DAILY_TEMPLATE.md)** - Daily workflow template (Polya's method)
- **This README** - Setup, daily index, and submission guidelines

These plans are standalone; existing `modules/*` in this repo can be used as optional references.

---

## Programme Philosophy: Definition Before Motion

> **"There is no algorithm for a problem you haven't defined."**  
> Progress is a vector: **definition** (direction) + **effort** (magnitude) = results

This programme follows **first principles thinking**: clarity before action, understanding before execution.

**Before every task, answer these four questions**:
1. **What exactly am I building/learning?** (Define the problem)
2. **What does success look like?** (Acceptance criteria)
3. **Why does this matter for production Django?** (Purpose)
4. **What constraints shape my approach?** (Limits)

**If you can't answer these clearly, stop and get clarity before coding.**

Every day follows **Polya's method**: Understand → Plan → Execute → Reflect (see [DAILY_TEMPLATE.md](intern_training/DAILY_TEMPLATE.md))

Read [PHILOSOPHY.md](intern_training/PHILOSOPHY.md) for complete training philosophy and anti-patterns to avoid.

---

### Programme outcomes

#### What you'll be able to do after this programme
- **Day 1 on the team**: Understand existing Django codebases; read and modify models, views, forms, and templates
- **Week 1 on the team**: Implement small features independently; write comprehensive tests; submit clean PRs with proper documentation
- **Month 1 on the team**: Own medium-sized features end-to-end with minimal supervision; participate effectively in code reviews
- **Technical competence**: Python fluency, OOP design mastery, DSA fundamentals, testing mindset, Django CRUD expertise
- **Professional skills**: Git workflows, collaborative development, problem decomposition, clear technical communication

#### Skills you'll master
- **Foundations-first confidence**: Linux, Git, shell, Python 3.12, OOP, data structures & algorithms, and systematic problem‑solving
- **Code quality discipline**: `black`, `isort`, `pylint`, type hints, docstrings, and security hygiene (secrets, validation, dependency management)
- **Testing mindset**: pytest mastery; write unit tests for core logic; TDD awareness; test coverage understanding
- **Data structures & algorithms**: Arrays, hashmaps, stacks, queues, trees, graphs; time/space complexity analysis; common patterns
- **Web literacy**: HTTP/REST fundamentals, HTML/CSS/JS basics to understand full-stack flows
- **Django readiness**: Project/app structure, ORM mastery, URL routing, templates, forms, CRUD operations, admin customization, basic auth
- **Data engineering basics**: CSV/JSON processing, validation, ETL pipelines, CLI tool development
- **Version Control and Team integration**: Git branching strategies, PR etiquette, code review participation, readable commits, comprehensive documentation

#### Deliverable
A production-ready Django CRUD application with:
- Clean architecture and separation of concerns
- Comprehensive unit test suite
- Proper error handling and validation
- Clear documentation and setup instructions
- Ready to be extended by the team on day one

### Programme plan (6-week fundamentals-first)
This pacing dedicates 4 weeks to fundamentals before Django, ensuring solid foundations for team integration.

**Week 1 — Systems + Python Basics**
- Linux, Git, shell workflows
- Python: data types, control flow, functions, modules
- Tooling: `black`, `isort`, `pylint`, type hints
- Problem-solving: 25-35 problems from ProblemBank_Python.md
- Weekend: Energy Insights CLI

**Week 2 — Python Advanced + OOP**
- Classes, inheritance, composition, dunder methods
- Dataclasses, encapsulation, design patterns
- Exceptions, file I/O, CSV/JSON processing
- Packaging and module organization
- Problem-solving: 20-25 problems from ProblemBank_OOP.md
- Weekend: Refactored package with OOP design

**Week 3 — Data Structures & Algorithms**
- Arrays, hashmaps, stacks, queues
- Sorting, searching, two pointers, sliding window
- Trees and graphs basics
- Time/space complexity analysis
- Problem-solving: 30-40 problems from ProblemBank_DSA.md
- Weekend: Algorithm implementations with tests

**Week 4 — Testing + Data Engineering**
- pytest mastery: fixtures, parametrization, mocking
- Data validation and ETL pipelines
- CLI tools with argparse
- HTTP/REST basics, Python `requests`
- Problem-solving: 15-20 problems from ProblemBank_DataHandling.md
- Weekend: Complete data pipeline with tests

**Week 5 — Django Foundations**
- Project setup, apps, settings, migrations
- Models, ORM, QuerySets (select_related/prefetch_related)
- URL routing, FBVs/CBVs, templates
- Forms, validation, CRUD operations
- Admin customization
- Problem-solving: 15-20 problems from ProblemBank_Django.md (models/views)
- Weekend: Task Tracker CRUD app

**Week 6 — Django Advanced + Integration**
- Authentication, permissions, per-user data
- Form validation, messages framework
- Pagination, search, filtering
- Django testing (models/views/forms)
- DRF basics (optional): simple REST API
- Problem-solving: 10-15 problems from ProblemBank_Django.md (auth/API/testing)
- Weekend: Production-ready Django app with auth + tests

### What you will need
- Python 3.12+
- A code editor (VS Code/PyCharm) with Python extension
- Git and GitHub account (SSH set up)
- Virtual environment (`python -m venv venv`)
- Formatters and linters: `black`, `isort`, `pylint`

### Quick setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
python -m pip install --upgrade pip
pip install black isort pylint

# Optional: store tool configs in your repo root
# Note: black uses 88 chars by default (PEP8), no need to configure
echo "[settings]\nprofile = black" > .isort.cfg
echo "[MASTER]\nignore=venv,.venv\n[FORMAT]\nmax-line-length=88" > .pylintrc

# Run locally when needed
black . && isort . && pylint **/*.py || true
```

### How to use these plans
- Follow the weekly plan above; each week has a corresponding `intern_training/weekXX.md` file with daily details.
- **Daily quota**: Solve 5-7 problems per day from the relevant Problem Bank (mix of Core, Stretch, Challenge).
- Every day includes: topics, hands-on tasks, problem-solving with tests, and deliverables.
- Weekends have a focused project assignment to consolidate the week's learning with **acceptance criteria** (promotion gate).
- Keep a daily log (`LEARNING.md`) of insights, gotchas, problem solutions, and links to your PRs.
- **Total problems**: 115-145 curated problems across 6 weeks.

### Weekly index (6-week plan)
- [week01.md](intern_training/week01.md): Systems + Python Basics
- [week02.md](intern_training/week02.md): Python Advanced + OOP
- [week03.md](intern_training/week03.md): Data Structures & Algorithms
- [week04.md](intern_training/week04.md): Testing + Data Engineering
- [week05.md](intern_training/week05.md): Django Foundations
- [week06.md](intern_training/week06.md): Django Advanced + Integration

### Daily detail
Use the per‑day plans under `intern_training/weekXX/` for granular tasks. All Week 3 (DSA) and Week 6 (Django Advanced) materials are fully updated and aligned with the programme.

### Sample data and inputs
- Logs for shell scripting tasks
  - Directory: `data/sample_logs/`
  - Files: `app.log`, `sys.log` (for filtering and archiving exercises)
- CSV for data tasks
  - File: `data/energy/hourly_prices.csv` (columns: `timestamp`, `price`)
  - Used in Week 1 Day 3 and Weekend CLI
- JSON for web basics
  - File: `data/web/energy_stats.json`
  - Used in Week 2 Day 2 (render via JS)
- Frontend template (bonus Week 5)
  - Directory: `frontend_template/` (index.html, styles.css, js/)
  - Used to scaffold the Week 5 frontend

### Practice exercises (supplemental)
- `intern_training/week01/day02_exercises.md`: Python fundamentals practice (optional)
- `week02/day01_exercises.md`: OOP fundamentals practice (mandatory for Week 2 gate)

### Problem banks (115 curated problems)
- **[ProblemBank_Python.md](intern_training/ProblemBank_Python.md)**: 25 problems (strings, lists, dicts, comprehensions, functions, file I/O)
- **[ProblemBank_OOP.md](intern_training/ProblemBank_OOP.md)**: 18 problems (classes, inheritance, composition, design patterns)
- **[ProblemBank_DSA.md](intern_training/ProblemBank_DSA.md)**: **35 problems** (arrays, stacks, queues, sorting, searching, two-pointers, sliding window, **5 core tree/recursion problems**, 2 graphs)
- **[ProblemBank_DataHandling.md](intern_training/ProblemBank_DataHandling.md)**: 15 problems (CSV/JSON processing, ETL pipelines, validation, testing)
- **[ProblemBank_Django.md](intern_training/ProblemBank_Django.md)**: 22 problems (models, views, forms, templates, admin, testing)

**Total: 115 problems** with sample inputs/outputs and complexity guidance.

**Bonus**: ProblemBank_DSA.md includes 21 additional **advanced/optional problems** for interview prep (not required for program).

**Note**: Legacy problem banks (ProblemBank_A, ProblemBank_B) have been removed. Use the new Problem Banks listed above.

**Structure**: Core (must), Stretch (nice), Challenge (bonus) for each bank.

**Daily quota**: 5-7 problems/day; submit solutions with tests and type hints; document learnings in `LEARNING.md`.

**Legacy exercise files** (still available):
- `intern_training/week01/day02_exercises.md`: Python fundamentals practice
- `intern_training/week02/day01_exercises.md`: OOP fundamentals practice

### Submitting daily work
- Open a PR in your playground repo named `weekXX-dayYY: <short-title>`.
- Include:
  - What you built (1–2 sentences)
  - Commands to run
  - Screenshots (if UI) or sample output
  - Confirm you ran: `black .`, `isort .`, `pylint **/*.py` (where applicable)

### Submission directory structure
For each day, in your playground repo create:
```
weekXX/
  dayYY/
    README.md        # Summary, commands, screenshots/outputs
    src/             # Code for the day
    tests/           # (if applicable)
    data/            # (if applicable; don't commit large files)
```
Example: `week02/day03/src/tasktracker/...`

For weekend assignments:
```
weekXX/
  weekend/
    README.md        # Acceptance criteria and demo
    src/
    tests/
    screenshots/     # (recommended)
```

Each weekend README should clearly show whether all acceptance criteria are met for promotion to the next week.


