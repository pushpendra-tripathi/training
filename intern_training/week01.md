## Week 1 — Linux, Git, Python Basics, Shell, Problem Solving

### Weekly learning goals
- Navigate Linux CLI confidently; write simple shell scripts.
- Understand Git branching and open clean PRs.
- Master Python basics: data types, control flow, functions, modules, typing mindset.
- Build habits in problem solving (daily practice) and writing small, testable scripts.

### Daily schedule

#### Day 1 (Mon): Linux + Git foundations
- Topics
  - Files/dirs, permissions, pipes and redirection, `grep`, `find`, `tar`.
  - Git: clone, branch, commit, push, PR; rebase vs merge at a high level.
- Hands-on
  - Create `scripts/backup_logs.sh` that archives a sample logs folder by date, keeps last N archives, and prints a summary.
  - Initialize a personal playground repo, commit the script, open a PR.
- Problem solving (45–60 min)
  - From LeetCode Easy: [Two Sum](https://leetcode.com/problems/two-sum/), [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- Deliverables
  - PR with the shell script and a brief `README.md`.

#### Day 2 (Tue): Python essentials I — data types and functions
- Topics
  - Numbers, strings, lists, tuples, dicts, sets; slicing; mutability; truthiness.
  - Functions, arguments, return values; modules and imports; standard library tour.
- Hands-on
  - Create `utils/` with `text.py` (cleaning, tokenizing) and `collections.py` (frequency map, de-duplication) with docstrings.
  - Configure `black`, `isort`, `pylint`; run them locally.
- Problem solving
  - From LeetCode Easy: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/), [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- Deliverables
  - Utilities committed; passes format and lint locally.

#### Day 3 (Wed): Control flow, errors, files
- Topics
  - Conditionals, loops, exceptions, context managers.
  - `pathlib`, JSON/CSV read/write.
- Hands-on
  - Build `tools/csv_stats.py` that loads a CSV and prints: row count, column summaries, top-N by a numeric column.
  - Add a `--file` and `--top` argument, and a basic usage example in README.
- Problem solving
  - From LeetCode Easy/Medium: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/), [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- Deliverables
  - Script runs on a sample CSV and outputs correct summaries; formatted and linted.

#### Day 4 (Thu): Shell scripting practice + Python packaging basics
- Topics
  - Bash functions, `set -euo pipefail`, quoting; simple Makefile targets.
  - Python package layout: `__init__.py`, `__main__.py` for CLI entry.
- Hands-on
  - Turn `csv_stats.py` into a small package `energy_insights/` with an executable entry point `python -m energy_insights`.
  - Add `Makefile` targets: `format` (black+isort), `lint` (pylint), `run`.
- Problem solving
  - From Project Euler: [Problem 1](https://projecteuler.net/problem=1), [Problem 2](https://projecteuler.net/problem=2)
- Deliverables
  - Package runs via module; Makefile commands work on a clean checkout.

#### Day 5 (Fri): DSA warmup and refactor
- Topics
  - Lists vs dicts vs sets; big-O intuition; sliding window and two-pointer patterns.
- Hands-on
  - Add unit tests for your helpers using `unittest` (standard lib) or `pytest` if preferred.
  - Refactor functions for clarity and early returns; ensure linters pass.
- Problem solving
  - From LeetCode Easy/Medium: [Binary Search](https://leetcode.com/problems/binary-search/), [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- Deliverables
  - Tests passing locally; code formatted and linted.

### Weekend assignment
Build the “Energy Insights” CLI as a small package that:
- Loads an hourly prices CSV and computes: daily averages, top-N spikes, basic anomaly detection (z-score threshold is fine).
- Provides a clean CLI: `--file`, `--metric`, `--top`, and pretty prints results.
- Includes `README.md` with install/run instructions and sample output.
- Quality gate: must pass `black`, `isort`, `pylint` locally and be easy to run from a fresh clone.

Suggested reference datasets: your own CSV or any public hourly/time-series sample.


