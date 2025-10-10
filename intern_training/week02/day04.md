## Week 2 · Day 4 — Packaging and CLI Ergonomics

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A polished, user-friendly CLI package with proper entrypoints, subcommands, help text, and error handling with exit codes.

**Why does this matter for Django?**  
Django management commands follow similar patterns. Understanding CLI design, argparse subcommands, and exit codes prepares you for building custom Django commands.

**What does success look like?**  
- Package installable with `python -m yourpkg` entrypoint
- Subcommands with helpful `--help` text
- Clear error messages with appropriate exit codes

---

### Objectives
- Improve your package layout and CLI usability (`__main__.py`, argparse, help, exit codes).

### Tasks
1) CLI structure
   - Add `__main__.py` to enable `python -m yourpkg` entrypoint.
   - Use `argparse` with subcommands and helpful `--help`.
2) Errors and exit codes
   - Map error conditions to non-zero exit codes and friendly messages.
3) Makefile targets
   - Ensure `make format`, `make lint`, and `make test` work from a clean clone.

### Expected Result
- CLI feels polished and self-documenting; bad inputs produce clear output and exit codes.

### Problem solving
- LeetCode: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- Project Euler: [Problem 4](https://projecteuler.net/problem=4)

### Outcomes
- A friendly CLI and stable package ergonomics.

### Deliverables
- CLI demo outputs and README usage examples.

### Submission checklist
- [ ] `python -m <pkg>` works with subcommands
- [ ] Error cases covered with exit codes
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


