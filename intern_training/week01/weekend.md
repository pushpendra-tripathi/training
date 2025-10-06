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
- **Example row**: `2022-01-01T00:00:00,45.23`

### Expected Output
Your CLI should produce:
1. **Daily Averages**: Table showing date and average price per day
   ```
   Date         Avg Price
   2022-01-01   $42.15
   2022-01-02   $38.92
   ```
2. **Top N Spikes**: Highest prices with timestamps
   ```
   Top 10 Price Spikes:
   2022-01-15T14:00:00  $125.50
   2022-02-03T18:00:00  $118.25
   ```
3. **Anomaly Detection**: Identify outliers using z-score (>2) or 95th percentile
   ```
   Anomalies detected: 12 hours
   ```

### Command-Line Interface
- `--file <path>`: CSV file path (required)
- `--metric <name>`: Column name to analyze (default: "price")
- `--top <n>`: Number of spikes to show (default: 10)
- `--help`: Show usage information

### Example Usage
```bash
python -m energy_insights --file data/hourly_prices.csv --metric price --top 5
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
- [ ] Handles bad inputs gracefully (missing file/column)A
- [ ] Clear, formatted output and simple code structure


