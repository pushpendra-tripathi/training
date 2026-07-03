## Week 1 · Weekend Assignment — Energy Insights CLI

### Objective
Package a clean, user-friendly CLI that analyzes a time-series CSV and outputs useful insights.

### Problem Statement
You work at an energy company that needs to analyze hourly energy price data. Your task is to build a command-line tool that:
- Reads hourly price data from a CSV file
- Calculates daily average prices
- Identifies the top N price spikes
- Detects anomalies (unusually high prices)

The tool should be user-friendly, handle errors gracefully, and produce clear, formatted output.

### Input Specification
- **Sample file**: `intern_training/data/energy/hourly_prices.csv`
- **CSV format**: Contains columns `timestamp` (ISO format) and `price` (float)
- **Example row**: `2025-09-30T00:00:00Z,38.4`
- **Note**: The shipped sample covers a single day (24 hourly rows). Your daily-averages table will show one row against this file — test multi-day grouping with a CSV of your own that spans several days.

### Expected Output
Your CLI should produce (using the shipped sample file):
1. **Daily Averages**: Table showing date and average price per day
   ```
   Date         Avg Price
   2025-09-30   $49.52
   ```
2. **Top N Spikes**: Highest prices with timestamps
   ```
   Top 3 Price Spikes:
   2025-09-30T17:00:00Z  $63.90
   2025-09-30T07:00:00Z  $61.00
   2025-09-30T16:00:00Z  $60.20
   ```
3. **Anomaly Detection**: Identify outliers using z-score (>2) or 95th percentile
   ```
   Anomalies detected: 1 hour (95th percentile threshold)
   ```

### Command-Line Interface
- `--file <path>`: CSV file path (required)
- `--metric <name>`: Column name to analyze (default: "price")
- `--top <n>`: Number of spikes to show (default: 10)
- `--help`: Show usage information

### Example Usage
```bash
python -m energy_insights --file intern_training/data/energy/hourly_prices.csv --metric price --top 3
```

### Step-by-step tasks
1) CLI arguments
   - Implement `--file`, `--metric`, `--top` with sensible defaults and help text.
2) Data loading
   - Parse timestamps; handle missing/invalid rows gracefully.
3) Analytics
   - Compute daily averages; identify top-N spikes; simple anomaly detection.
4) Output formatting
   - Pretty-print tables to console; ensure readability.
5) Docs
   - README includes setup, usage, and an example command with sample output.
6) Quality
   - Run `black .`, `isort .`, `pylint **/*.py` locally; fix issues.

### Constraints
- Code must pass `black`, `isort`, and `pylint` when run locally.
- Include `README.md` with setup and usage examples; provide one sample CSV or a link.

### Acceptance criteria (promotion to Week 2)
- CLI runs against the sample CSV and prints correct stats.
- Handles invalid inputs with clear errors.
- Code structure is simple and readable; package runs via `python -m`.
- README is complete; formatting/linting pass locally.

### Submission checklist
- [ ] Works from a fresh clone with documented steps
- [ ] Handles bad inputs gracefully (missing file/column)
- [ ] Clear, formatted output and simple code structure


