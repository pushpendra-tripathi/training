## Week 6 — Django Advanced + Integration

### Weekly learning goals
- Implement Django authentication and per-user data access
- Master advanced form validation and UX patterns
- Build pagination, search, and filtering features
- Create RESTful APIs with Django REST Framework (optional)
- Optimize QuerySets and database queries
- Prepare Django apps for production deployment

### Daily schedule

#### Day 1 (Mon): Authentication & Authorization
- Topics
  - Django auth system: User model, login/logout, signup
  - Authentication views and templates
  - LoginRequired decorator and mixins
  - Per-user data filtering
  - Messages framework for auth flows
- Hands-on
  - Add login/logout views and templates
  - Restrict views to authenticated users
  - Add owner field to Task model
  - Filter QuerySets by request.user
  - Solve 2-3 auth problems from ProblemBank_Django.md
- Problem solving
  - Core: Auth flows, per-user filtering
  - Stretch: Custom user model, permission-based access
- Deliverables
  - Auth working; unauthorized access blocked; per-user data isolated

#### Day 2 (Tue): Advanced Forms & Validation
- Topics
  - Custom form validation: clean methods, validators
  - Form wizards and multi-step forms
  - Formsets for multiple objects
  - AJAX form submission
  - Client-side + server-side validation coordination
- Hands-on
  - Add complex validation rules to Task form
  - Implement formsets for batch task creation
  - Add inline validation feedback
  - Solve 2-3 advanced form problems
- Problem solving
  - Core: Custom validation, formsets
  - Stretch: AJAX form submission, form wizards
- Deliverables
  - Advanced validation working; formsets functional; UX polished

#### Day 3 (Wed): Pagination, Search & Filtering
- Topics
  - Django Paginator: page objects, page navigation
  - Q objects for complex queries
  - SearchVector for full-text search
  - Filtering with django-filter (optional)
  - URL query parameters for state
- Hands-on
  - Add pagination to list view (10 per page)
  - Implement search by title/description
  - Add filters for status, due_date range
  - Preserve filters/search in pagination links
  - Solve 2 pagination/search problems
- Problem solving
  - Core: Pagination, search, filtering
  - Stretch: Complex queries with Q objects
- Deliverables
  - List view with working pagination, search, filters; URL state preserved

#### Day 4 (Thu): REST API with Django REST Framework (Optional) OR Query Optimization
- Topics (Option A: DRF)
  - DRF serializers and viewsets
  - Routers and URL configuration
  - Authentication for APIs (token/session)
  - API permissions and throttling
- Topics (Option B: Optimization)
  - select_related and prefetch_related
  - Database indexes
  - Query profiling with django-debug-toolbar
  - Caching strategies
- Hands-on (Option A)
  - Create API endpoints for Task CRUD
  - Add serializer validation
  - Test with HTTPie/Postman
- Hands-on (Option B)
  - Optimize queries with select_related
  - Add database indexes
  - Measure query improvements
  - Solve 2 optimization problems
- Deliverables
  - API functional OR queries optimized; benchmarks documented

#### Day 5 (Fri): Testing, Documentation & Deployment Prep
- Topics
  - Integration testing for auth flows
  - Testing APIs (if applicable)
  - Static files collection
  - Environment variables and settings management
  - Basic deployment checklist (DEBUG=False, ALLOWED_HOSTS, etc.)
- Hands-on
  - Write integration tests for complete user flows
  - Test API endpoints (if applicable)
  - Configure settings for production
  - Create deployment documentation
  - Solve 1-2 testing problems
- Problem solving
  - Core: Integration tests, API tests
  - Stretch: Deployment configuration
- Deliverables
  - Comprehensive test suite; deployment docs; production settings configured

### Weekend assignment
**Production-Ready Django Application**

Build a fully-featured, deployment-ready Task Tracker:

1. **Authentication**:
   - User registration, login, logout
   - Password reset (email simulation)
   - Per-user task isolation
2. **Features**:
   - Full CRUD with ownership checks
   - Pagination (10 per page)
   - Search by title/description
   - Filters: status, date range, tags
   - Bulk actions (mark multiple as done)
3. **Forms**:
   - Robust validation with clear error messages
   - Inline validation feedback
   - Success/error messages throughout
4. **Admin**:
   - Fully configured with all useful features
   - Custom actions
   - Inline editing
5. **API (Optional)**:
   - RESTful endpoints for tasks
   - Token authentication
   - Proper HTTP status codes
6. **Performance**:
   - Optimized queries (select_related/prefetch_related)
   - Database indexes on frequently queried fields
   - Query count benchmarks documented
7. **Testing**:
   - >90% coverage
   - Unit tests for models, views, forms
   - Integration tests for user flows
   - API tests (if applicable)
8. **Documentation**:
   - Comprehensive README
   - API documentation (if applicable)
   - Deployment guide
   - Architecture diagram
   - Screenshots/demo GIF
9. **Production-Ready**:
   - Environment variables for secrets
   - DEBUG=False configuration
   - Static files collected
   - Basic security headers

**Acceptance criteria:**
- All features functional and tested
- 10+ advanced Django problems solved from ProblemBank
- Authentication working with proper isolation
- Pagination, search, filtering working
- Test coverage >90%
- Production configuration complete
- Documentation comprehensive
- Code quality tools pass

### Suggested problems (10-15 total for the week)
- See `intern_training/ProblemBank_Django.md` - focus on auth, API, testing, optimization sections
- Daily quota: 2-3 problems (focus on advanced patterns)

### Final promotion gate (program completion)
- Production-ready Django application deployed or deployment-ready
- 10+ advanced Django problems solved
- All features functional with comprehensive tests
- Performance optimized and benchmarked
- Complete documentation
- Weekend assignment meets all criteria
- Ready for team integration on Day 1




