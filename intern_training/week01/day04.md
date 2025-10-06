## Week 1 · Day 4 — Shell Scripting Practice + Python Packaging

### Objectives
- Write safer bash scripts and convert a Python script into an installable module entry point.

### Prerequisites
- Day 3 CSV stats script completed.

### Tasks
1) Shell scripting
   - Add safety: `set -euo pipefail` at the top of scripts.
   - Use functions and positional args with validation; print help on `-h/--help`.
2) Package your CLI
   - Create `energy_insights/` package and move CSV logic into it.
   - Add `__main__.py` so it runs with `python -m energy_insights --help`.
   - Function specs (inside package)
     - `compute_daily_averages(rows: list[dict[str, str]], ts_col: str, value_col: str) -> dict[str, float]`
       - Input: rows, timestamp column, numeric value column
       - Output: mapping `YYYY-MM-DD` -> average float
     - `find_spikes(rows: list[dict[str, str]], value_col: str, top: int) -> list[dict[str, str]]`
       - Input: rows, numeric value column, number of spikes
       - Output: top entries by value
3) Makefile convenience
   - Add `Makefile` targets: `format` (black+isort), `lint` (pylint), `run` (example command).

### Problem solving (45–60 min)
- Project Euler: [Problem 1](https://projecteuler.net/problem=1), [Problem 2](https://projecteuler.net/problem=2)

### Outcomes
- Executable Python module with simple automation scripts.

### Deliverables
- `energy_insights/` package with `__main__.py` and documented CLI options.
- `Makefile` with working targets.

### Submission checklist
- [ ] Running `python -m energy_insights --help` shows usage
- [ ] Makefile targets work on a fresh clone
- [ ] Code formatted (`black`/`isort`) and linted (`pylint`)


