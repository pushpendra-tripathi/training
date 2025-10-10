## Problem Bank B — OOP, I/O, error handling

Format: Provide typed functions/classes and tests. Show sample inputs/outputs and error cases.

### Core (must)
1) Design `Task` and `TaskManager` (composition)
   - Input: create tasks with title, status, due_date
   - Output: `TaskManager.list_by_status("todo") -> [Task(...), ...]`
   - Tests: creation, equality, status transitions, and list filtering
2) CSV ingestion with required columns
   - Input (CSV):
     ```
     title,status,due_date
     Pay bills,todo,2025-01-01
     Grocery,done,
     ```
   - Output: List[Task]; invalid rows raise `InvalidRowError` with row number
3) JSON ingestion with schema validation
   - Input (JSON):
     ```json
     [{"title":"Pay bills","status":"todo","due_date":"2025-01-01"}]
     ```
   - Output: List[Task]; collect multiple errors with a combined message
4) CLI summary
   - Command: `python -m energy_insights --file tasks.csv --top 2`
   - Output (stdout):
     ```
     Top statuses:
     todo: 10
     done: 7
     ```

### Stretch (nice)
5) Plugin interface
   - Input: `--format yaml` loads `yaml` plugin if installed
   - Output: Same API returns parsed tasks
6) Logging and verbosity
   - Input: `--verbose`
   - Output: INFO logs for steps; DEBUG for parsed counts

### Challenge (bonus)
7) Property-based tests
   - Input: random lists; function `normalize_titles`
   - Property: idempotent; preserves multiset of words
8) Recovery from corrupt input
   - Input: CSV with a corrupt line
   - Output: Skip with warning; continue processing rest; return summary with error count

### Guidance
- Use type hints and docstrings; raise clear exceptions; test happy/sad paths.

