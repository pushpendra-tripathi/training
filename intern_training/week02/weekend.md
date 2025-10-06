## Week 2 · Weekend Assignment — Polished Task Tracker

### Objective
Consolidate CRUD, admin, templates, and validation into a small, usable Django app.

### Problem Statement
Build a production-ready Task Tracker Django application that allows users to:
- Create, read, update, and delete tasks
- Search tasks by title
- Filter tasks by due date
- View tasks in a paginated list
- Manage tasks through Django admin with custom actions

The app should have proper validation, user-friendly error messages, and a clean UI.

### Expected Features

#### 1. Task Model
- **Fields**: `title` (str, max 200), `description` (text, optional), `status` (choice: Todo/In-Progress/Done), `due_date` (date, optional), `created_at` (auto)
- **Validation**: 
  - Title cannot be empty
  - Status transitions: Todo → In-Progress → Done (prevent invalid jumps)
  - Due date must be in the future for new tasks

#### 2. Task List View
- **URL**: `/tasks/`
- **Features**:
  - Display tasks in cards/table with title, status badge, due date
  - Search: `?q=meeting` searches in title
  - Filter: `?due_before=2025-12-31` shows tasks due before date
  - Pagination: 10 tasks per page with Previous/Next links
- **Example**: `/tasks/?q=review&due_before=2025-11-01&page=2`

#### 3. CRUD Operations
- **Create** (`/tasks/create/`): Form with all fields, show validation errors
- **Detail** (`/tasks/<id>/`): Show all task details with Edit/Delete buttons
- **Update** (`/tasks/<id>/edit/`): Pre-filled form, prevent invalid status transitions
- **Delete** (`/tasks/<id>/delete/`): Confirmation page before deletion

#### 4. Django Admin
- **List display**: title, status (colored), due_date, created_at
- **Filters**: status, due_date (past/upcoming)
- **Search**: by title
- **Custom action**: "Mark selected as Done" (bulk update status)

#### 5. Seed Data
- Management command or fixture to create:
  - 1 demo user (`demo`/`demo123`)
  - 10 sample tasks with various statuses and due dates

### Example UI Flow
```
1. Visit /tasks/ → See list of 10 tasks
2. Click "New Task" → Fill form → Submit → Redirected to list with success message
3. Search "meeting" → See filtered results
4. Click task → See details → Click Edit → Update status → See updated task
5. Admin at /admin/ → Select 3 tasks → Mark as Done → Verify bulk update
```

### Step-by-step tasks
1) Status workflow
   - Add `status` choices: Todo, In-Progress, Done; prevent invalid transitions in form clean.
2) Search and filter
   - Implement title search (`?q=`) and due-date filter (`?due_before=YYYY-MM-DD`).
3) Pagination
   - Paginate list view (e.g., 10 per page) with page controls.
4) Admin polish
   - Add list display, filters, search; implement one custom action (e.g., mark selected as Done).
5) Seed data
   - Provide a fixture or simple management command to create a demo user and 10 tasks.
6) Docs and screenshots
   - Update README with setup steps, screenshots of CRUD and admin, and common commands.
7) Quality
   - Run `black .`, `isort .`, and `pylint **/*.py` locally; fix issues.

### Acceptance criteria (promotion to Week 3)
- CRUD works end-to-end; invalid transitions are blocked with clear messages.
- Search/filter work together and pagination is functional.
- Admin is usable with the custom action verified.
- Seed script/fixture creates data successfully and is documented.
- README is complete; formatting and linting pass locally.

### Submission checklist
- [ ] CRUD + search + filters working
- [ ] Admin useful for day-to-day operations
- [ ] Formatting/lint clean


