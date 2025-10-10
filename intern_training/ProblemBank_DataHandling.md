## Problem Bank — Data Handling & Testing (15 problems)

**Target**: Week 4. Pick 3-5 problems daily; focus on real-world data processing.

### Core (must) — CSV Processing

1) **Read CSV and calculate statistics**
   - Input: sales.csv with columns [date, product, quantity, price]
   - Output: total_revenue, avg_sale, top_product
   - Handle: missing values, malformed rows

2) **Filter CSV by criteria**
   - Input: employees.csv, filter by department="Engineering" and salary>80000
   - Output: filtered.csv
   - Use: csv.DictReader/DictWriter

3) **Merge two CSV files**
   - Input: customers.csv (id, name), orders.csv (id, customer_id, total)
   - Output: merged.csv (customer_name, order_total)
   - Handle: missing customer IDs

4) **CSV validation**
   - Input: data.csv with expected schema [name:str, age:int, email:str]
   - Output: List of validation errors with row numbers
   - Rules: age>0, email format, required fields
   ```python
   errors = validate_csv("data.csv", schema)
   # [{"row": 3, "error": "Invalid email format"},
   #  {"row": 5, "error": "Age must be positive"}]
   ```

5) **Aggregate CSV data**
   - Input: transactions.csv with [timestamp, user_id, amount]
   - Output: daily_summary.csv with [date, total_transactions, total_amount]
   - Group by date

### Core (must) — JSON Processing

6) **Parse nested JSON**
   - Input: API response with nested user/posts/comments
   - Output: flattened list of comments with user info
   ```json
   {"users": [{"id":1,"name":"Alice","posts":[{"id":10,"comments":[...]}]}]}
   ```

7) **JSON schema validation**
   - Input: config.json
   - Schema: required fields, type validation, range checks
   - Output: list of validation errors or None
   ```python
   schema = {
       "api_key": {"type": str, "required": True},
       "timeout": {"type": int, "min": 1, "max": 300}
   }
   validate_json(data, schema)
   ```

8) **Convert JSON to CSV**
   - Input: users.json (list of dicts)
   - Output: users.csv
   - Handle: missing keys, nested objects (flatten or skip)

9) **JSON data transformation**
   - Input: raw_data.json
   - Transform: rename keys, parse dates, calculate derived fields
   - Output: processed_data.json
   ```python
   # Transform: "created_at" -> datetime object
   #           "full_name" -> from "first_name" + "last_name"
   ```

### Stretch (nice) — Data Pipelines

10) **ETL Pipeline**
    - Extract: Read from CSV
    - Transform: Clean, validate, enrich
    - Load: Write to JSON and database (SQLite)
    - Error handling: collect and log all errors
    ```python
    pipeline = ETLPipeline(source="data.csv", target="output.json")
    stats = pipeline.run()
    # {"processed": 100, "errors": 3, "duration": "1.2s"}
    ```

11) **Data deduplication**
    - Input: records.json with potential duplicates
    - Logic: fuzzy matching on name, exact on email
    - Output: unique_records.json + duplicates_report.json

12) **Time series resampling**
    - Input: hourly_data.csv
    - Output: daily_aggregates.csv (sum, mean, min, max)
    - Handle: missing timestamps, timezone conversion

### Challenge (bonus) — Testing & Quality

13) **Property-based testing**
    - Function: normalize_text(s: str) -> str
    - Properties: idempotent, preserves word count, lowercase
    - Use: hypothesis library
    ```python
    from hypothesis import given, strategies as st
    
    @given(st.text())
    def test_normalize_idempotent(s):
        assert normalize_text(normalize_text(s)) == normalize_text(s)
    ```

14) **Fixture factory pattern**
    - Create pytest fixtures for sample CSV/JSON data
    - Parametrize tests across multiple data variants
    - Use: tmp_path fixture for file I/O tests
    ```python
    @pytest.fixture
    def sample_csv(tmp_path):
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("name,age\nAlice,30\nBob,25")
        return csv_file
    ```

15) **Integration test: full pipeline**
    - Test end-to-end: raw CSV → validated JSON → database
    - Assertions: row counts, data integrity, error handling
    - Use: temporary databases, cleanup with fixtures
    ```python
    def test_pipeline_integration(sample_csv, tmp_db):
        result = run_pipeline(sample_csv, tmp_db)
        assert result.success == True
        assert query_db(tmp_db, "SELECT COUNT(*) FROM users") == 2
    ```

### Guidance
- **Error handling**: Never silently fail; log or raise with context
- **Validation**: Collect all errors before raising (don't fail on first error)
- **Type hints**: Use pathlib.Path, List, Dict, Optional
- **Testing**:
  - Use tmp_path for file I/O tests
  - Parametrize tests for multiple scenarios
  - Test happy path + error cases
  - Aim for >90% coverage
- **Performance**: Profile large file processing; use generators for memory efficiency
- **Logging**: Add structured logging for debugging pipelines


