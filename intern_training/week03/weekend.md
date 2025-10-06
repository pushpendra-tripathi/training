## Week 3 · Weekend Assignment — API-first Enhancements

### Objective
Extend the Task Tracker API with filtering and tests, keeping setup simple.

### Problem Statement
Build a RESTful API for the Task Tracker using Django REST Framework that supports:
- Full CRUD operations for tasks
- Advanced filtering by status and date ranges
- Proper validation with helpful error messages
- Comprehensive test coverage
- Clear API documentation

The API should follow REST conventions and provide a good developer experience.

### Expected API Endpoints

#### 1. List Tasks (GET /api/tasks/)
```bash
# Basic list
GET /api/tasks/

# Filter by status
GET /api/tasks/?status=todo

# Filter by date range
GET /api/tasks/?due_before=2025-12-31&due_after=2025-01-01

# Combine filters
GET /api/tasks/?status=in_progress&due_before=2025-11-15
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the API implementation",
    "status": "in_progress",
    "due_date": "2025-11-15",
    "created_at": "2025-10-01T10:00:00Z"
  }
]
```

#### 2. Create Task (POST /api/tasks/)
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New task",
    "description": "Task description",
    "status": "todo",
    "due_date": "2025-12-01"
  }'
```

**Success** (201 Created): Returns created task
**Validation Error** (400 Bad Request):
```json
{
  "title": ["This field is required."],
  "due_date": ["Date must be in the future."],
  "status": ["Invalid choice. Must be one of: todo, in_progress, done"]
}
```

#### 3. Retrieve Task (GET /api/tasks/<id>/)
**Response** (200 OK): Single task object
**Not Found** (404): `{"detail": "Not found."}`

#### 4. Update Task (PUT/PATCH /api/tasks/<id>/)
**Success** (200 OK): Returns updated task
**Validation Error** (400 Bad Request): Field-specific errors

#### 5. Delete Task (DELETE /api/tasks/<id>/)
**Success** (204 No Content): Empty response
**Not Found** (404): Error message

### Validation Requirements
- **title**: Required, 1-200 characters
- **description**: Optional, max 1000 characters
- **status**: Required, must be one of: `todo`, `in_progress`, `done`
- **due_date**: Optional, must be in future for new tasks, valid ISO date format

### Test Coverage
Write tests for each endpoint covering:

#### Happy Paths
- List all tasks successfully
- Create task with valid data
- Retrieve existing task
- Update task with valid changes
- Delete existing task
- Filter by status returns correct results
- Filter by date range works correctly

#### Error Cases
- Create with missing required fields
- Create with invalid date format
- Create with due_date in past
- Update non-existent task (404)
- Delete non-existent task (404)
- Invalid status choice
- Filter with invalid date format

### Example Test Structure
```python
class TaskAPITests(TestCase):
    def test_create_task_success(self):
        # Test successful task creation
        
    def test_create_task_missing_title(self):
        # Test validation error for missing title
        
    def test_filter_by_status(self):
        # Test status filtering works
```

### Step-by-step tasks
1) Filtering
   - Add `status`, `due_before`, `due_after` query params for `/api/tasks/`.
2) Validation
   - Validate date formats and return helpful error messages.
3) Tests
   - For each endpoint, write one success and one failure test (permissions, validation).
4) Docs
   - Add curl/HTTPie examples in README and describe parameters.
5) Quality
   - Run `black .`, `isort .`, and `pylint **/*.py` locally; fix issues.

### Acceptance criteria (promotion to Week 4)
- Filters function correctly and reject invalid input with clear errors.
- Tests cover happy and sad paths; all pass locally.
- README updated with copy-pasteable commands.

### Submission checklist
- [ ] Filters work and are documented
- [ ] Tests cover happy and sad paths
- [ ] Formatting/linting pass locally


