## Week 4 · Day 2 — Database Fundamentals + Data Validation

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A relational database schema with proper constraints/indexes, plus an ETL pipeline that validates and loads data into SQLite with transactions.

**Why does this matter for Django?**  
Django ORM abstracts SQL, but understanding database design, normalization, constraints, and transactions is critical for building efficient Django models and avoiding data integrity issues.

**What does success look like?**  
- Database schema with constraints (PK, FK, NOT NULL) and indexes
- ETL pipeline loading to database with transaction support
- Validation module collecting all errors, not just the first

---

### Objectives
- Understand relational database concepts and SQL basics
- Master database design: normalization, constraints, indexes
- Build robust schema validation for CSV/JSON
- Implement transactions and proper error handling

### Tasks

#### Part 1: Database Fundamentals (Morning)

1) **SQL Basics with SQLite**
   - Install: SQLite comes with Python (sqlite3 module)
   - Create database and tables: CREATE TABLE
   - CRUD operations: INSERT, SELECT, UPDATE, DELETE
   - Queries: WHERE, ORDER BY, LIMIT, OFFSET
   - Aggregations: COUNT, SUM, AVG, MIN, MAX, GROUP BY
   - Joins: INNER JOIN, LEFT JOIN (basic understanding)

2) **Database Design**
   - **Normalization**:
     - 1NF: Atomic values, no repeating groups
     - 2NF: No partial dependencies
     - 3NF: No transitive dependencies
     - When to denormalize (performance vs. redundancy)
   - **Relationships**:
     - One-to-Many: Foreign Key
     - Many-to-Many: Junction table
     - One-to-One (rare)
   - **Entity-Relationship Diagrams** (ERD): Basic notation

3) **Constraints**
   - PRIMARY KEY: Unique identifier
   - FOREIGN KEY: Referential integrity
   - UNIQUE: Ensure uniqueness
   - NOT NULL: Required fields
   - CHECK: Value validation
   - DEFAULT: Default values

4) **Indexes**
   - What: Data structure for faster lookups
   - When: Frequently queried columns, foreign keys
   - Trade-offs: Read speed vs. write speed and storage
   - CREATE INDEX, EXPLAIN QUERY PLAN

5) **Transactions**
   - ACID properties: Atomicity, Consistency, Isolation, Durability
   - BEGIN, COMMIT, ROLLBACK
   - Use cases: Multiple related operations
   - Python context manager: automatic commit/rollback

6) **Python sqlite3 Module**
   - Connection and cursor objects
   - Execute queries with parameterized statements (prevent SQL injection)
   - Fetch results: fetchone(), fetchall(), fetchmany()
   - Context manager for automatic cleanup
   - Example:
     ```python
     import sqlite3
     
     with sqlite3.connect('db.sqlite3') as conn:
         cursor = conn.cursor()
         cursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", 
                       ("Task 1", "todo"))
         conn.commit()
     ```

7) **Hands-on Practice**
   - Create tasks database with proper schema:
     - tasks table (id, title, description, status, created_at)
     - categories table (id, name)
     - tasks_categories junction table (task_id, category_id)
   - Add constraints: PKs, FKs, NOT NULL
   - Create indexes on frequently queried fields
   - Implement CRUD operations with parameterized queries
   - Use transactions for multi-step operations

#### Part 2: Data Validation & ETL (Afternoon)

1) **Schema Validation**
   - Define schemas for CSV/JSON data
   - Required fields, type checking, range validation
   - Collect ALL errors (don't fail on first error)
   - Clear error messages with row/field context

2) **CSV Processing**
   - Read CSV with DictReader
   - Validate schema and data types
   - Handle missing values, malformed rows
   - Write validated data with DictWriter

3) **JSON Processing**
   - Parse nested JSON structures
   - Schema validation (required fields, types, ranges)
   - Transform and flatten nested objects
   - Write validated JSON

4) **ETL Pipeline Integration**
   - **Extract**: Read from CSV, JSON, or API
   - **Transform**:
     - Clean data (strip whitespace, normalize)
     - Validate against schema
     - Enrich with derived fields
     - Handle missing/malformed data
   - **Load**: Write to JSON and SQLite database with:
     - Proper schema and constraints
     - Indexes on queried fields
     - Transactions for atomicity
     - Error rollback

5) **Problem solving (3-4 problems from ProblemBank_DataHandling.md)**
   - Core: Create database schema with constraints
   - Core: CSV validation with schema
   - Core: JSON schema validation
   - Stretch: ETL Pipeline with database loading
   - Challenge: Transaction rollback on validation errors

### Outcomes
- Understand relational database fundamentals
- Write SQL queries confidently
- Design normalized database schemas
- Use constraints and indexes appropriately
- Implement transactions for data integrity
- Validate data with comprehensive error reporting
- Build ETL pipelines loading to databases

### Deliverables
- **Database practice** (`database_practice.py`):
  - Create tasks database with schema
  - Constraints: PK, FK, NOT NULL, UNIQUE
  - Indexes on status and created_at
  - CRUD operations with parameterized queries
  - Transaction examples
  - Tests for all operations
- **Validation module** (`validators.py`):
  - CSV schema validator
  - JSON schema validator
  - Error collection and reporting
  - Tests with malformed data
- **ETL pipeline** (`pipeline.py`):
  - Extract from multiple sources
  - Transform with validation
  - Load to JSON + SQLite
  - Use transactions
  - Comprehensive error handling
  - Tests for each step
- **Database ERD**: Diagram showing tables and relationships
- **SQL examples**: Document with sample queries

### Submission checklist
- [ ] Database schema created with constraints
- [ ] Indexes on appropriate fields
- [ ] CRUD operations with parameterized queries
- [ ] Transactions implemented correctly
- [ ] Validation module with comprehensive tests
- [ ] ETL pipeline loads to database
- [ ] Error handling collects all errors
- [ ] 3+ data handling problems solved
- [ ] Test coverage >85%
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them

### Resources
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python sqlite3 docs](https://docs.python.org/3/library/sqlite3.html)
- [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)
- [SQL Injection Prevention](https://bobby-tables.com/python)


