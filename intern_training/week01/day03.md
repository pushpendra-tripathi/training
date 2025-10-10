## Week 1 · Day 3 — Control Flow, Errors, Files, CSV Stats

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A CSV analysis script that safely reads files, handles errors gracefully, and provides statistical summaries.

**Why does this matter for Django?**  
Django apps process user data (CSV uploads, API inputs). Proper error handling prevents crashes and data corruption.

**What does success look like?**  
A working CLI that processes valid CSVs AND handles invalid inputs with clear error messages (not crashes).

---

### Objectives
- Use conditionals, loops, exceptions, and context managers effectively.
- Read/write CSV and JSON files; build a CLI script with arguments.

### Prerequisites
- Day 2 utilities; local black/isort/pylint available.

### Tasks
1) Control flow and errors (deep dive)
   - **Conditionals**: if/elif/else, ternary expressions, truthy/falsy values
   - **Loops**: for, while, `break`, `continue`, `else` clause on loops
   - **Comprehensions**: list, dict, set comprehensions with conditions
   - **Exceptions**: try/except/else/finally, raising exceptions, custom exceptions
   - **Context managers**: `with` statement, understanding `__enter__` and `__exit__`
   - Practice: Implement safe parsing and error handling with `try/except` and early returns.
2) CSV stats script (simple CLI)
   - Create `tools/csv_stats.py` with **basic** CLI args: `--file <path>`, `--top <n>`, `--column <name>`.
   - Output: row count, numeric column summary (min/max/mean), and top-N rows by the selected column.
   - Use `argparse` for simple argument parsing (no subcommands, logging, or config - just basics).
   - Use `pathlib` for file handling.
   - Use sample input: `intern_training/data/energy/hourly_prices.csv` with `--column price`.
   - **Note**: This is a simple introduction to argparse; Week 4 will cover professional CLI design.
   - Function specs
     - `load_csv(file_path: str) -> list[dict[str, str]]`
       - Input: path to CSV
       - Output: list of rows as dicts (string values)
     - `summarize_numeric(rows: list[dict[str, str]], column: str) -> dict[str, float]`
       - Input: rows and a numeric column name
       - Output: `{ "min": float, "max": float, "mean": float }`
     - `top_n(rows: list[dict[str, str]], column: str, n: int) -> list[dict[str, str]]`
       - Input: rows, numeric column, number N
       - Output: top N rows sorted descending by the column
3) Documentation
   - Update project README with usage examples and sample output.

### Problem solving (45–60 min)
- LeetCode: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/), [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

### Outcomes
- A robust CLI script handling invalid inputs gracefully with clear messages.

### Deliverables
- `tools/csv_stats.py` committed and formatted (`black`/`isort`), linted (`pylint`).
- README examples and a small sample CSV in `data/` (optional).

### Submission checklist
- [ ] CLI accepts args and prints results
- [ ] Handles missing files/columns with helpful errors
- [ ] Formatted and linted cleanly
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Execution log maintained
  - [ ] Learning reflection documented
  - [ ] Connection to Django explained


