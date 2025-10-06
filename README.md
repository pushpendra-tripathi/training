## Intern Training Program (4 Weeks + Bonus Week 5)

This folder contains a complete, self-contained Django intern training package. It includes week-by-week lesson plans with daily tasks, built-in problem-solving practice, and weekend assignments with **promotion gates** at the end of each week.

### Quick Links
- **[TRAINING.md](intern_training/TRAINING.md)** - High-level overview and ground rules
- **[STRUCTURE.md](intern_training/STRUCTURE.md)** - Program structure, gates, and learning progression
- **This README** - Setup, daily index, and submission guidelines

These plans are standalone; existing `modules/*` in this repo can be used as optional references.

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
- Follow [week01.md](week01.md) through [week04.md](week04.md) in order.
- Every day includes: topics, hands-on tasks, problem-solving (LeetCode/Project Euler), function specs (where applicable), and deliverables.
- Weekends have a focused assignment to consolidate the week's learning with **acceptance criteria** (promotion gate).
- Keep a daily log (`LEARNING.md`) of insights, gotchas, and links to your PRs.
- Week 5 ([week05.md](week05.md)) is an optional bonus week for fullstack integration (requires passing Week 4 gate).

### Directory
- [week01.md](intern_training/week01.md): Linux, Git, Python fundamentals, shell scripting, DSA warmup
- [week02.md](intern_training/week02.md): OOP, web basics, Django project setup, CRUD, admin, templates
- [week03.md](intern_training/week03.md): Django auth, forms, validations, simple REST API (DRF), testing basics
- [week04.md](intern_training/week04.md): Templates consolidation, CRUD polish, testing basics
- [week05.md](intern_training/week05.md) (bonus): Fullstack integration (Django API + Frontend)

### Daily index
- Week 1
  - [Day 1 — Linux + Git Foundations](intern_training/week01/day01.md)
  - [Day 2 — Python Essentials I + Local Quality Tools](intern_training/week01/day02.md)
  - [Day 3 — Control Flow, Errors, Files, CSV Stats](intern_training/week01/day03.md)
  - [Day 4 — Shell Scripting + Packaging](intern_training/week01/day04.md)
  - [Day 5 — DSA Warmup + Refactor and Test](intern_training/week01/day05.md)
  - [Weekend — Energy Insights CLI](intern_training/week01/weekend.md)
- Week 2
  - [Day 1 — OOP and Packaging](intern_training/week02/day01.md)
  - [Day 2 — Web Basics (HTML, CSS, JS)](intern_training/week02/day02.md)
  - [Day 3 — Django Project Setup](intern_training/week02/day03.md)
  - [Day 4 — Models, Admin, CRUD](intern_training/week02/day04.md)
  - [Day 5 — Templates, Validation, UX Polish](intern_training/week02/day05.md)
  - [Weekend — Polished Task Tracker](intern_training/week02/weekend.md)
- Week 3
  - [Day 1 — Auth and Per-User Data](intern_training/week03/day01.md)
  - [Day 2 — Forms and Validation](intern_training/week03/day02.md)
  - [Day 3 — Simple REST API with DRF](intern_training/week03/day03.md)
  - [Day 4 — Testing Basics](intern_training/week03/day04.md)
  - [Day 5 — Pagination and Simple Performance](intern_training/week03/day05.md)
  - [Weekend — API-first Enhancements](intern_training/week03/weekend.md)
- Week 4
  - [Day 1 — Templates Deep Dive](intern_training/week04/day01.md)
  - [Day 2 — Forms, Messages, and Validation](intern_training/week04/day02.md)
  - [Day 3 — List Pagination, Search, and Sorting](intern_training/week04/day03.md)
  - [Day 4 — Admin Polish and Template Customization](intern_training/week04/day04.md)
  - [Day 5 — Testing Basics and Template Refinements](intern_training/week04/day05.md)
  - [Weekend — Templates and Admin Consolidation](intern_training/week04/weekend.md)
- Week 5 (Bonus)
  - [Fullstack Overview](intern_training/week05.md)
  - [Day 1 — Frontend Scaffold + API Consumption](intern_training/week05/day01.md)
  - [Day 2 — Auth Integration and Secure Calls](intern_training/week05/day02.md)
  - [Day 3 — Create/Update Flows and Form UX](intern_training/week05/day03.md)
  - [Day 4 — UI Polish and State Management](intern_training/week05/day04.md)
  - [Day 5 — E2E Sanity and Docs](intern_training/week05/day05.md)
  - [Weekend — Fullstack Mini Demo](intern_training/week05/weekend.md)

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


