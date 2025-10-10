## Week 5 — Django Foundations

### Weekly learning goals
- Set up Django project structure and understand the framework architecture
- Master models and ORM: queries, relationships, migrations
- Build views (FBVs and CBVs) and URL routing
- Create templates with inheritance and Django template language
- Implement forms and validation
- Customize Django admin for productivity
- Write tests for models and views

### Daily schedule

#### Day 1 (Mon): Project Setup + Models & ORM
- Topics
  - Django project vs. app structure
  - Settings configuration, SECRET_KEY, DATABASES
  - Models: fields, relationships (ForeignKey, ManyToMany)
  - Migrations: makemigrations, migrate, showmigrations
  - QuerySets: filter, get, all, order_by
- Hands-on
  - Create `tasktracker` project and `tasks` app
  - Define `Task` model with title, description, status, due_date, created_at
  - Create and run migrations
  - Django shell: practice QuerySet operations
  - Solve 3-4 model problems from ProblemBank_Django.md
- Problem solving
  - Core: Blog Post model, Custom model manager
  - Stretch: Model with choices, Many-to-Many relationship
- Deliverables
  - Project structure created; models defined; migrations working; QuerySet practice documented

#### Day 2 (Tue): Views & URL Routing
- Topics
  - Function-Based Views (FBVs) vs. Class-Based Views (CBVs)
  - URL patterns, path(), include(), URL parameters
  - ListView, DetailView, CreateView, UpdateView, DeleteView
  - Request/Response cycle
  - Context data and template rendering
- Hands-on
  - Implement CRUD views for Task model
  - URL routing with named patterns
  - Solve 3-4 view problems from ProblemBank_Django.md
- Problem solving
  - Core: FBV List, CBV ListView, Detail View with slug
  - Stretch: Create View with validation, Update and Delete Views
- Deliverables
  - CRUD views working; URLs configured; named patterns used; reverse() working

#### Day 3 (Wed): Templates & Django Template Language
- Topics
  - Template inheritance: base.html, blocks, extends
  - Template includes and partials
  - Template tags: {% url %}, {% static %}, {% csrf_token %}
  - Template filters: date, truncatechars, custom filters
  - Context processors
- Hands-on
  - Create base template with navigation
  - Build list and detail templates
  - Add template includes for reusable components
  - Solve 2-3 template problems from ProblemBank_Django.md
- Problem solving
  - Core: Template inheritance system, Custom template tags
  - Stretch: Template with context processors
- Deliverables
  - Template system working; base + extends pattern; partials extracted; custom filter added

#### Day 4 (Thu): Forms & Validation + Admin
- Topics
  - ModelForm: Meta class, fields, widgets
  - Form validation: clean methods, field validators
  - Messages framework: success/error messages
  - Admin: ModelAdmin, list_display, list_filter, search_fields
  - Admin actions and customization
- Hands-on
  - Create ModelForm for Task
  - Add custom validation (e.g., due_date in future)
  - Configure admin with filters and search
  - Add custom admin action (bulk status change)
  - Solve 3-4 form/admin problems from ProblemBank_Django.md
- Problem solving
  - Core: ModelForm with custom validation, Form with multiple models
  - Stretch: Custom admin configuration, Inline admin
- Deliverables
  - Forms working with validation; messages displaying; admin configured and useful

#### Day 5 (Fri): Testing Django Applications
- Topics
  - Django TestCase vs. pytest-django
  - Testing models, views, forms
  - Test client: GET, POST requests
  - Fixtures and setUpTestData
  - Testing templates and context
- Hands-on
  - Write tests for Task model
  - Write tests for CRUD views
  - Write tests for form validation
  - Solve 2-3 testing problems from ProblemBank_Django.md
- Problem solving
  - Core: Model tests, View tests, Form tests
  - Stretch: Integration test full CRUD flow
- Deliverables
  - Test suite covering models, views, forms; tests passing; coverage >80%

### Weekend assignment
**Task Tracker CRUD Application**

Build a production-quality Django CRUD app:

1. **Models**:
   - Task model with validations
   - At least one related model (e.g., Category, Tag)
   - Custom manager for published/archived tasks
2. **Views**:
   - Full CRUD using CBVs
   - List with pagination (10 per page)
   - Search by title
   - Filter by status
3. **Templates**:
   - Base template with navigation
   - List, detail, create, update, delete templates
   - Partials for task cards
   - Messages framework integrated
4. **Forms**:
   - ModelForm with custom validation
   - Clear error display
5. **Admin**:
   - Configured with list_display, filters, search
   - At least one custom admin action
6. **Tests**:
   - Model tests (creation, methods, managers)
   - View tests (list, detail, create, update, delete)
   - Form tests (valid/invalid data)
   - Coverage >80%
7. **Documentation**:
   - README with setup instructions
   - Screenshots of key pages
   - Model diagram

**Acceptance criteria:**
- All CRUD operations functional
- 15+ Django problems solved from ProblemBank
- Forms validate correctly with clear errors
- Admin is useful and customized
- Test suite passes with >80% coverage
- Code quality tools pass
- README is clear and complete

### Suggested problems (15-20 total for the week)
- See `intern_training/ProblemBank_Django.md` - focus on models, views, forms, templates, admin sections
- Daily quota: 3-4 problems (focus on understanding Django patterns)

### Promotion gate (advance to Week 6 if all met)
- CRUD application functional and tested
- 15+ Django problems solved
- Forms and validation working correctly
- Admin customized and productive
- Test coverage >80%
- Weekend assignment complete with all criteria
- Quality gates pass


