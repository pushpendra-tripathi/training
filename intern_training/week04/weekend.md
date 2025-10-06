## Week 4 · Weekend Assignment — Templates and Admin Consolidation

### Objective
Consolidate the template-driven UI and admin into a polished, demo-ready app.

### Problem Statement
Refine the Task Tracker into a production-quality Django application with:
- Clean, DRY templates using inheritance and reusable components
- Professional UI with consistent styling and user feedback
- Feature-rich list view (pagination, search, sorting)
- Power-user admin interface with custom actions
- Comprehensive test coverage for all views

This is the final polish before the app is ready for real users.

### Expected UI/UX Quality

#### 1. Template Structure (DRY Principle)
```
templates/
  base.html              # Main layout with nav, messages, footer
  tasks/
    _task_card.html      # Reusable task display partial
    _task_form.html      # Reusable form partial
    list.html            # Extends base, includes _task_card
    detail.html          # Extends base, clean layout
    form.html            # Extends base, includes _task_form
```

#### 2. Base Layout Features
- **Navigation**: Logo, Home, Tasks, New Task, Admin (if staff), Logout
- **Messages area**: Success (green), Error (red), Warning (yellow) with auto-dismiss
- **Footer**: Copyright, version, helpful links
- **Responsive**: Works on mobile and desktop

#### 3. Task List View (`/tasks/`)
**Features**:
- **Search bar**: "Search by title..." input, searches on submit
- **Filters**: Due date range picker, status dropdown
- **Sorting**: Click column headers to sort by title, status, or due_date (asc/desc)
- **Pagination**: "Showing 1-10 of 45 tasks" with Prev/Next and page numbers
- **Empty state**: "No tasks found. Create your first task!"
- **Task cards**: Title (link), status badge, due date with color (red if overdue), description preview

**URL Examples**:
```
/tasks/                                    # All tasks, first page
/tasks/?q=meeting                          # Search
/tasks/?status=todo&due_before=2025-12-31  # Filtered
/tasks/?sort=due_date&order=asc&page=2     # Sorted and paginated
```

#### 4. Task Detail View (`/tasks/<id>/`)
- Clean card layout with all fields
- Status badge (colored: todo=gray, in_progress=blue, done=green)
- Due date with relative time ("Due in 3 days" or "Overdue by 2 days")
- Action buttons: Edit (blue), Delete (red), Back to List
- Timestamps: Created and last updated

#### 5. Task Form (Create/Edit)
- All fields with placeholders and help text
  - Title: "Enter a descriptive title" (required)
  - Description: "Optional details..." (textarea)
  - Status: Dropdown with descriptions
  - Due date: Date picker (HTML5 date input)
- Validation errors displayed above field in red
- Non-field errors at top of form
- Submit button: "Create Task" or "Update Task"
- Cancel link back to list

#### 6. Django Admin Enhancements
**List Display**:
- Columns: ☐ (checkbox), Title, Status (colored), Due Date, Created
- Colored status: Custom method with colored spans
- Date hierarchy: By due_date

**Filters** (right sidebar):
- Status (all, todo, in_progress, done)
- Due date (today, this week, this month, overdue)
- Created date

**Search**: By title and description

**Custom Actions**:
- "Mark selected as Done" (bulk update)
- "Mark selected as In Progress"
- "Export to CSV" (bonus)

**Inline Editing**: Quick edit without leaving list view

#### 7. Visual Polish
- **Colors**: Consistent color scheme (primary, success, danger, warning)
- **Typography**: Clear hierarchy (h1, h2, body text)
- **Spacing**: Comfortable padding and margins
- **Buttons**: Consistent style with hover states
- **Forms**: Clear focus states, good spacing
- **Messages**: Toast/alert style with icons

### Example User Journey
```
1. Land on /tasks/ → See 10 tasks in cards, search bar, filters
2. Type "meeting" in search → Submit → See filtered results
3. Click "Due Date" column → List re-sorts ascending
4. Click task title → See detail page with all info
5. Click "Edit" → See pre-filled form
6. Change status to "Done" → Submit → Redirect to list with success message
7. Visit /admin/tasks/task/ → See rich list with filters
8. Select 3 tasks → Choose "Mark as Done" → Confirm → See success
9. Take screenshots of: list, detail, form, admin list, admin action
```

### Step-by-step tasks
1) Templates
   - Ensure base layout, partials, and custom filters are used across pages.
2) List and detail
   - Verify pagination, search, and sorting on list; ensure detail page is clear and styled.
3) Forms
   - Confirm validation messages are clear; add help texts and placeholders where helpful.
4) Admin
   - Verify filters, search, and the custom action; capture a screenshot of action in use.
5) Docs
   - Update README with setup, testing, and screenshots of key pages.
6) Quality
   - Run `black .`, `isort .`, and `pylint **/*.py` locally; fix issues.

### Acceptance criteria (promotion to Week 5 bonus)
- UI is consistent and DRY; list/search/pagination/sorting work as documented.
- Admin is productive and shows the custom action working.
- README is complete with screenshots and commands; formatting/linting pass locally.


