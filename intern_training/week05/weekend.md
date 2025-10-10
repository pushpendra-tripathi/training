## Week 5 · Weekend — Task Tracker CRUD Application

### Overview
Build a production-quality Django CRUD application demonstrating mastery of Django fundamentals.

### Requirements

#### 1. Models (with relationships)
- **Task Model** with fields:
  - title (CharField, max 200, required)
  - description (TextField, optional)
  - status (CharField with choices: TODO, IN_PROGRESS, DONE)
  - priority (CharField with choices: LOW, MEDIUM, HIGH)
  - due_date (DateField, optional)
  - created_at (auto_now_add)
  - updated_at (auto_now)
  - `__str__` method returning title
  - Meta ordering by priority, then due_date
  - Custom manager: completed_tasks, pending_tasks

- **Category Model** (related model):
  - name (CharField, unique)
  - description (TextField, optional)
  - Task ForeignKey relationship

- **Tag Model** (optional, ManyToMany):
  - name (CharField)
  - Task ManyToMany relationship

#### 2. Views (Complete CRUD)
Implement using Class-Based Views:
- **ListView**: 
  - Display all tasks
  - Pagination (10 per page)
  - Filter by status, priority
  - Search by title
- **DetailView**: Display single task with all details
- **CreateView**: Form to create new task
- **UpdateView**: Form to edit existing task
- **DeleteView**: Confirmation before deletion
- All views with success messages

#### 3. Templates (DRY with inheritance)
- **base.html**:
  - HTML5 structure
  - Navigation menu
  - Messages display area
  - Blocks: title, content, extra_css, extra_js
- **task_list.html**:
  - Table or cards displaying tasks
  - Pagination controls
  - Search form
  - Filter links (by status, priority)
- **task_detail.html**:
  - All task information
  - Edit/Delete buttons
- **task_form.html**:
  - For both create and update
  - Display form errors clearly
- **task_confirm_delete.html**:
  - Confirmation message
  - Cancel/Confirm buttons
- **Partials**:
  - `_task_card.html`: reusable task display
  - `_pagination.html`: pagination controls
  - `_messages.html`: messages display

#### 4. Forms & Validation
- **TaskForm(ModelForm)**:
  - All task fields
  - Custom validation:
    - Title minimum 3 characters
    - due_date must be in future (if provided)
    - Custom error messages
  - Widget customization (optional)

#### 5. Admin Configuration
- **TaskAdmin**:
  - list_display: title, status, priority, due_date, created_at
  - list_filter: status, priority, created_at
  - search_fields: title, description
  - date_hierarchy: created_at
  - ordering: ['-created_at']
  - Custom action: "Mark as Done" (bulk action)
- **CategoryAdmin**: Basic configuration
- **Inline editing** for Tags (optional)

#### 6. Testing (>80% coverage)
- **Model Tests** (`tests/test_models.py`):
  - Task creation
  - `__str__` method
  - Custom managers
  - Validation
- **View Tests** (`tests/test_views.py`):
  - List view returns 200
  - Detail view with valid/invalid ID
  - Create view POST creates task
  - Update view modifies task
  - Delete view removes task
  - Pagination works
  - Search works
- **Form Tests** (`tests/test_forms.py`):
  - Valid data passes
  - Invalid data fails with errors
  - Custom validation works
- **Coverage**: `coverage run manage.py test && coverage report`

#### 7. Features
- **Pagination**: 10 tasks per page
- **Search**: By title (case-insensitive)
- **Filtering**: By status, by priority
- **Sorting**: By due_date, by priority
- **Messages**: Success/error messages for all actions
- **Responsive**: Basic mobile-friendly layout

#### 8. Documentation
- **README.md**:
  - Project description
  - Setup instructions:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```
  - Features list
  - Screenshots of key pages
  - Model diagram (relationships)
  - Running tests instructions
- **requirements.txt**: Django and dependencies
- **Model diagram**: Visual showing relationships

### Suggested Structure
```
week05/
  weekend/
    README.md
    requirements.txt
    tasktracker/              # Django project
      __init__.py
      settings.py
      urls.py
      wsgi.py
    tasks/                    # Django app
      __init__.py
      models.py               # Task, Category models
      views.py                # CBVs for CRUD
      forms.py                # TaskForm
      admin.py                # Admin configuration
      urls.py                 # App URLs
      templatetags/
        task_filters.py       # Custom template filters
      templates/
        base.html
        tasks/
          task_list.html
          task_detail.html
          task_form.html
          task_confirm_delete.html
        partials/
          _task_card.html
          _pagination.html
          _messages.html
      static/
        css/
          style.css
        js/
          (optional)
      tests/
        __init__.py
        test_models.py
        test_views.py
        test_forms.py
    manage.py
    db.sqlite3 (gitignored)
```

### Acceptance Criteria
- [ ] **Models**: Task + Category with relationship
- [ ] **Migrations**: All applied successfully
- [ ] **CRUD**: All operations functional
- [ ] **Templates**: Base + inheritance working
- [ ] **Forms**: Validation with error display
- [ ] **Admin**: Customized and useful
- [ ] **Pagination**: 10 per page
- [ ] **Search**: By title working
- [ ] **Filtering**: By status and priority
- [ ] **Messages**: Success/error feedback
- [ ] **Tests**: >80% coverage, all passing
- [ ] **Documentation**: README with setup + screenshots
- [ ] **Code Quality**: Passes black, isort, pylint
- [ ] **Problems**: 15+ Django problems solved from ProblemBank

### Promotion Gate
To advance to Week 6, you must:
- ✅ Meet all acceptance criteria above
- ✅ Application fully functional
- ✅ Test coverage >80%
- ✅ Admin customized and productive
- ✅ Code quality tools pass
- ✅ 15+ Django problems solved
- ✅ Documentation complete with screenshots

### Tips
- Start with models and migrations
- Test models before building views
- Build one view at a time (list → detail → create → update → delete)
- Use CBVs to minimize boilerplate
- Test as you build, don't save for last
- Make admin useful - you'll use it for data entry


