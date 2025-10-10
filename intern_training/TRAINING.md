## 6‑Week Django Intern Training (Fundamentals-First)

> **Quick Links**: [Main README](../README.md) | [STRUCTURE.md](STRUCTURE.md) | This Overview

This is the lightweight, shareable overview. The complete day‑by‑day lesson plans with tasks, problem solving (115-145 curated problems), and weekend assignments:

- **Week 1**: Systems + Python Basics (25-35 problems) — see `intern_training/week01.md`
- **Week 2**: Python Advanced + OOP (20-25 problems) — see `intern_training/week02.md`
- **Week 3**: Data Structures & Algorithms (30-40 problems) — see `intern_training/week03.md`
- **Week 4**: Testing + Data Engineering (15-20 problems) — see `intern_training/week04.md`
- **Week 5**: Django Foundations (15-20 problems) — see `intern_training/week05.md`
- **Week 6**: Django Advanced + Integration (10-15 problems) — see `intern_training/week06.md`

You may use existing `modules/*` content in this repo as optional references, but the new plans are self‑contained.

### Problem Banks (115 Curated Problems)
- `ProblemBank_Python.md`: 25 problems (Python fundamentals)
- `ProblemBank_OOP.md`: 18 problems (OOP, design patterns)
- `ProblemBank_DSA.md`: **35 problems** (arrays, stacks, queues, sorting, searching, patterns, **5 tree/recursion intro**, 2 graphs)
  - *Bonus: 21 advanced tree/graph problems are optional*
- `ProblemBank_DataHandling.md`: 15 problems (CSV/JSON, ETL, validation, testing)
- `ProblemBank_Django.md`: 22 problems (models, views, forms, templates, admin, DRF)

**Note**: Legacy problem banks (ProblemBank_A, ProblemBank_B) moved to `legacy/` folder.

### Ground rules and setup (Day 0)
- Environment
  - Install Python 3.12+, and create a virtual environment (`python -m venv .venv`).
  - Create a working repo: `intern-<name>-playground` on GitHub.
  - Install and configure local quality tools: `black`, `isort`, `pylint`.
- Git/GitHub
  - Configure SSH keys and your user settings.
  - Use feature branches and open small, focused PRs to `main`.
  - Write clear, imperative commit messages.

### Daily workflow (Polya's method)

Every day follows **Understand → Plan → Execute → Reflect**:

1. **Morning (Before coding)**: Answer problem definition questions
   - What exactly am I building today?
   - Why does this matter for production Django?
   - What does success look like?
   - Use [DAILY_TEMPLATE.md](DAILY_TEMPLATE.md) to structure thinking

2. **During work**: Execute systematically
   - Follow daily plan from template
   - Log decisions and blockers
   - Ask for help promptly when blocked >30 min; articulate the problem definition and what you tried

3. **Evening (After coding)**: Reflect on learning
   - Did I achieve today's objective?
   - What patterns did I learn?
   - How does this connect to Django?
   - Complete reflection in daily log

### Daily problem solving
- **Daily quota**: 5-7 problems from the relevant Problem Bank (mix of Core, Stretch, Challenge)
- **Weekly total**: 25-40 problems depending on difficulty
- **Submissions**: Include tests, type hints, and complexity analysis in docstrings
- **Reflection**: MANDATORY - Use [DAILY_TEMPLATE.md](DAILY_TEMPLATE.md) for structured reflection

### Weekend assignments
- Each week ends with a project assignment that consolidates the week's learning
- Deliverables specified in `intern_training/weekXX/weekend.md`
- Acceptance criteria define the promotion gate

### Practical milestones and promotion gates (6-week)
- **Week 1 → Week 2**: CLI working; 25+ Python problems solved with tests; quality tools pass
- **Week 2 → Week 3**: OOP package complete; 20+ OOP problems solved; pytest suite passing
- **Week 3 → Week 4**: 30+ DSA problems solved; complexity analysis documented; algorithm implementations tested
- **Week 4 → Week 5**: ETL pipeline working; 15+ data problems solved; comprehensive tests pass
- **Week 5 → Week 6**: CRUD app functional; 15+ Django problems solved; model/view tests pass
- **Week 6 (final)**: Production-ready app with auth; 10+ advanced problems solved; deployment-ready with docs


### References
- Python: [Official Tutorial](https://docs.python.org/3/tutorial/)
- Django: [Official Docs](https://docs.djangoproject.com/en/stable/)
- DRF: [Django REST Framework](https://www.django-rest-framework.org/)
- Git: [Pro Git](https://git-scm.com/book/en/v2), [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- Linux/Shell: [Linux Journey](https://linuxjourney.com/), [Bash Guide](https://mywiki.wooledge.org/BashGuide)

