## 6‑Week Django Intern Training (Fundamentals-First)

> **Quick Links**: [Main README](../README.md) | [STRUCTURE.md](STRUCTURE.md) | This Overview

This is the lightweight, shareable overview. The complete day‑by‑day lesson plans with tasks, problem solving (97-126 curated problems), and weekend assignments:

- **Week 1**: Systems + Python Basics (20-25 problems) — see `intern_training/week01.md`
- **Week 2**: Python Advanced + OOP (15-18 problems) — see `intern_training/week02.md`
- **Week 3**: Data Structures & Algorithms (25-35 problems) — see `intern_training/week03.md`
- **Week 4**: Testing + Data Engineering (12-15 problems) — see `intern_training/week04.md`
- **Week 5**: Django Foundations (15-19 problems) — see `intern_training/week05.md`
- **Week 6**: Django Advanced + Integration (10-14 problems) — see `intern_training/week06.md`

These plans are self‑contained.

### Problem Banks (127 Curated Problems)
- `ProblemBank_Python.md`: 25 problems (Python fundamentals)
- `ProblemBank_OOP.md`: 18 problems (OOP, design patterns)
- `ProblemBank_DSA.md`: **35 problems** (arrays, stacks, queues, sorting, searching, patterns, **5 tree/recursion intro**, 2 graphs)
  - *Bonus: 21 advanced tree/graph problems are optional*
- `ProblemBank_DataHandling.md`: 15 problems (CSV/JSON, ETL, validation, testing)
- `ProblemBank_Django.md`: 34 problems (models, views, forms, templates, admin, auth, REST API (DRF), testing)

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
- **Daily quota**: See each week's overview for its exact pace (mix of Core, Stretch, Challenge)
- **Weekly total**: 10-35 problems depending on difficulty and bank size
- **Submissions**: Include tests, type hints, and complexity analysis in docstrings
- **Reflection**: MANDATORY - Use [DAILY_TEMPLATE.md](DAILY_TEMPLATE.md) for structured reflection

### Weekend assignments
- Each week ends with a project assignment that consolidates the week's learning
- Deliverables specified in `intern_training/weekXX/weekend.md`
- Acceptance criteria define the promotion gate

### Practical milestones and promotion gates (6-week)
- **Week 1 → Week 2**: CLI working; 20+ Python problems solved with tests; quality tools pass
- **Week 2 → Week 3**: OOP package complete; 15+ OOP problems solved; pytest suite passing
- **Week 3 → Week 4**: 25+ DSA problems solved; complexity analysis documented; algorithm implementations tested
- **Week 4 → Week 5**: ETL pipeline working; 12+ data problems solved; comprehensive tests pass
- **Week 5 → Week 6**: CRUD app functional; 15+ Django problems solved; model/view tests pass
- **Week 6 (final)**: Full-stack app with auth, REST API, and frontend; 10+ advanced problems solved; complete docs


### References
- Python: [Official Tutorial](https://docs.python.org/3/tutorial/)
- Django: [Official Docs](https://docs.djangoproject.com/en/stable/)
- DRF: [Django REST Framework](https://www.django-rest-framework.org/)
- Git: [Pro Git](https://git-scm.com/book/en/v2), [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- Linux/Shell: [Linux Journey](https://linuxjourney.com/), [Bash Guide](https://mywiki.wooledge.org/BashGuide)

