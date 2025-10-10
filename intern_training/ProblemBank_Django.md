## Problem Bank — Django Fundamentals (20 problems)

**Target**: Weeks 5-6. Pick 4-5 problems daily; build incrementally on one project.

### Core (must) — Models & ORM

1) **Blog Post model**
   - Fields: title, content, author (ForeignKey to User), created_at, updated_at, published
   - Validations: title max 200 chars, content required
   - Methods: `__str__`, is_published
   ```python
   class Post(models.Model):
       title = models.CharField(max_length=200)
       # ... implement with validations
   ```

2) **Custom model manager**
   - Create PublishedManager that filters published=True
   - Usage: `Post.published.all()`
   - Add: ordering by -created_at

3) **Model with choices**
   - Task model with status choices: TODO, IN_PROGRESS, DONE
   - Priority choices: LOW, MEDIUM, HIGH
   - Default: status=TODO, priority=MEDIUM

4) **Many-to-Many relationship**
   - Models: Post, Tag
   - Relationship: Post can have multiple Tags
   - Query: all posts with tag "python"
   - Add: through model for custom attributes

5) **QuerySet optimization**
   - Query: Get all posts with author name (avoid N+1)
   - Use: select_related for ForeignKey
   - Query: Get all posts with their tags
   - Use: prefetch_related for ManyToMany

### Core (must) — Views & URLs

6) **Function-Based View: List**
   - URL: `/posts/`
   - Display: all published posts
   - Template: post_list.html
   - Add: pagination (10 per page)

7) **Class-Based View: ListView**
   - Convert FBV to CBV using ListView
   - Add: queryset filtering, context data
   - Override: get_queryset for custom logic

8) **Detail View with slug**
   - URL: `/posts/<slug:slug>/`
   - Display: single post
   - Handle: 404 if not found or not published

9) **Create View with validation**
   - URL: `/posts/create/`
   - Form: PostForm with validation
   - Success: redirect to post detail
   - Error: re-render form with errors

10) **Update and Delete Views**
    - URLs: `/posts/<pk>/edit/`, `/posts/<pk>/delete/`
    - Permission: only author can edit/delete
    - Delete: require confirmation page

### Stretch (nice) — Forms & Validation

11) **ModelForm with custom validation**
    - Form: PostForm
    - Clean method: title cannot contain profanity
    - Custom validator: future_date_validator for due_date

12) **Form with multiple models**
    - Create Post with Tags in one form
    - Use: formsets or custom save logic
    - Handle: validation across related objects

13) **AJAX form submission**
    - Submit form without page reload
    - Return: JSON response {success, errors}
    - Display: errors inline with JavaScript

### Stretch (nice) — Templates

14) **Template inheritance system**
    - base.html with blocks: title, content, sidebar
    - post_list.html extends base
    - Include partials: _post_card.html

15) **Custom template tags**
    - Tag: `{% get_recent_posts 5 %}`
    - Filter: `{{ text|markdown }}`
    - Use: register in templatetags/

16) **Template with context processors**
    - Add site_name, user_notifications to all templates
    - Create custom context processor

### Stretch (nice) — Admin

17) **Custom admin configuration**
    - List display: title, author, created_at, published
    - Filters: published, created_at
    - Search: title, content
    - Actions: bulk publish/unpublish

18) **Inline admin**
    - Edit Tags inline when editing Post
    - Use: TabularInline or StackedInline

### Challenge (bonus) — Testing

19) **Model tests**
    - Test: Post creation, str method, is_published
    - Test: QuerySet methods
    - Use: Django TestCase, fixtures
    ```python
    class PostModelTest(TestCase):
        def test_post_creation(self):
            post = Post.objects.create(...)
            self.assertEqual(post.title, "Test")
    ```

20) **View tests**
    - Test: list view returns 200
    - Test: detail view with valid/invalid slug
    - Test: create view requires login
    - Use: Client, reverse()

21) **Form tests**
    - Test: valid form data
    - Test: invalid form data (validation errors)
    - Test: custom clean methods

22) **Integration test: full CRUD flow**
    - Create → Read → Update → Delete
    - Assertions: database state, redirects, messages
    - Use: Django test client

### Guidance
- **Migrations**: Run `makemigrations` and `migrate` after model changes
- **Type hints**: Use django-stubs for better type checking
- **Testing**:
  - Use TestCase for database tests
  - Use setUpTestData for shared fixtures
  - Test views with self.client
  - Test forms in isolation
  - Aim for >80% coverage
- **Best practices**:
  - Use reverse() for URLs in tests/code
  - Avoid hardcoded IDs
  - Use get_object_or_404()
  - Add __str__ to all models
  - Use Django messages framework
- **Security**:
  - CSRF protection on forms
  - User authentication/authorization
  - Input validation
  - SQL injection prevention (use ORM)
- **Performance**:
  - Use select_related/prefetch_related
  - Add database indexes
  - Use pagination
  - Cache where appropriate


