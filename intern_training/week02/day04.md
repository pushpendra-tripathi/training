## Week 2 · Day 4 — Models, Admin, CRUD

### Objectives
- Define Django models, run migrations, customize admin, and implement CRUD with CBVs.

### Tasks
1) Model and migration
   - Define a `Task` model with these fields:
     - `title`: String field (max 200 characters)
     - `description`: Text field (optional)
     - `status`: Choice field with options: Todo, In-Progress, Done (default: Todo)
     - `due_date`: Date field (optional)
     - `created_at`: Auto-set timestamp on creation
     - `updated_at`: Auto-update timestamp on modification
   - Add a `Meta` class to order tasks by most recent first
   - Implement `__str__()` method to return the task title
   - Create and run migrations to apply the model to the database
   - Create a superuser account for admin access

2) Admin customization
   - Register the Task model in the Django admin
   - Customize the admin interface to show:
     - Useful columns in the list view (title, status, due_date, created_at)
     - Filters for status and due_date
     - Search capability on title and description
     - Date hierarchy for easier navigation
   - Test the admin by creating 5-10 sample tasks with varied data

3) CRUD with Class-Based Views
   - Implement CRUD operations using Django's Class-Based Views:
     - **List**: Display all tasks with pagination (10 per page)
     - **Create**: Form to add new tasks
     - **Update**: Form to edit existing tasks
     - **Delete**: Confirmation page before deletion
   - Set up URL patterns for all CRUD operations:
     - `/tasks/` - list view
     - `/tasks/create/` - create view
     - `/tasks/<id>/edit/` - update view
     - `/tasks/<id>/delete/` - delete view
   - Create templates for:
     - List view with pagination controls
     - Form view (shared for create and update)
     - Delete confirmation page
   - Configure success redirects to return to the list view

### Expected Result
- Admin interface is functional with custom list display, filters, and search
- You can create, view, edit, and delete tasks through the web interface
- Pagination works when there are more than 10 tasks
- All CRUD operations redirect appropriately after completion

### Problem solving (45–60 min)
- LeetCode: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- Project Euler: [Problem 4](https://projecteuler.net/problem=4)

### Outcomes
- End-to-end CRUD and a usable admin interface.

### Deliverables
- Screenshots of admin and CRUD pages; README instructions updated.

### Submission checklist
- [ ] CRUD works for Task model
- [ ] Admin shows useful columns and filters
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


