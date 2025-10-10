## Week 5 · Day 1 — Project Setup + Models & ORM

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A Django task tracker app with properly designed models, relationships, migrations, and QuerySet practice.

**Why does this matter for Django?**  
Models are the foundation of Django apps. Understanding fields, relationships, migrations, and the ORM is essential for building any Django application.

**What does success look like?**  
- Django project and app structure created correctly
- Task model with appropriate fields and relationships
- Comfortable using QuerySet API for CRUD operations

---

### Objectives
- Set up Django project structure correctly
- Master models, fields, relationships, and migrations
- Practice QuerySet operations and database queries

### Tasks
1) Django Project Setup
   - Install Django: `pip install django`
   - Create project: `django-admin startproject tasktracker`
   - Create app: `python manage.py startapp tasks`
   - Configure settings: INSTALLED_APPS, DATABASES, SECRET_KEY
   - Understand project vs. app structure

2) Model Design
   - Define `Task` model with fields:
     - title (CharField, max_length=200)
     - description (TextField, blank=True)
     - status (CharField with choices: TODO, IN_PROGRESS, DONE)
     - due_date (DateField, null=True, blank=True)
     - created_at (DateTimeField, auto_now_add=True)
     - updated_at (DateTimeField, auto_now=True)
   - Add `__str__` method
   - Add Meta class for ordering

3) Migrations
   - Create migrations: `python manage.py makemigrations`
   - Review migration files
   - Apply migrations: `python manage.py migrate`
   - Understand migration system

4) Django ORM Practice
   - Create superuser: `python manage.py createsuperuser`
   - Django shell: `python manage.py shell`
   - QuerySet operations:
     - Create: `Task.objects.create(...)`
     - Read: `.all()`, `.get()`, `.filter()`, `.exclude()`
     - Update: `.update()`, instance.save()
     - Delete: `.delete()`
     - Ordering: `.order_by()`
     - Filtering: field lookups (__exact, __contains, __gte, etc.)

5) Relationships
   - Add Category model (optional)
   - ForeignKey relationship: Task → Category
   - ManyToMany relationship example

6) Problem solving (3-4 problems from ProblemBank_Django.md)
   - Core: Blog Post model
   - Core: Custom model manager
   - Stretch: Model with choices
   - Stretch: Many-to-Many relationship

### Outcomes
- Django project properly structured
- Models designed with appropriate fields
- Migrations working correctly
- QuerySet operations mastered

### Deliverables
- `tasktracker` project created
- `tasks` app with Task model
- Migrations applied successfully
- Django shell practice documented (sample queries + outputs)
- 3-4 model problems solved with tests

### Submission checklist
- [ ] Project structure created
- [ ] Task model defined with all fields
- [ ] Migrations created and applied
- [ ] QuerySet practice documented
- [ ] 3+ model problems solved
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


