## Week 6 — Django Advanced + Integration

### Weekly learning goals
- Implement Django authentication and per-user data access
- Master advanced form validation and UX patterns
- Build pagination, search, and filtering features
- Create RESTful APIs with Django REST Framework
- Integrate a JavaScript frontend with the Django REST API

### Daily schedule

#### Day 1 (Mon): Authentication & Authorization
- Topics
  - Django auth system: User model, login/logout, signup
  - Authentication views and templates
  - Password reset (simulated via console email backend)
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
  - Form widgets: custom rendering, HTML5 date picker, custom attrs
  - Formsets for multiple objects
  - AJAX form submission
  - Client-side + server-side validation coordination
- Hands-on
  - Add complex validation rules to Task form
  - Customize form widget rendering
  - Implement formsets for batch task creation
  - Add inline validation feedback
  - Solve 2-3 advanced form problems
- Problem solving
  - Core: Custom validation, formsets
  - Stretch: AJAX form submission
- Deliverables
  - Advanced validation working; formsets functional; UX polished

#### Day 3 (Wed): Pagination, Search & Filtering
- Topics
  - Django Paginator: page objects, page navigation
  - Q objects for complex queries (OR/AND/NOT)
  - Case-insensitive search with `__icontains`
  - URL query parameters for state
- Hands-on
  - Add pagination to list view (10 per page)
  - Implement search by title/description with Q objects
  - Add filters for status, priority, date range
  - Preserve filters/search in pagination links
  - Solve 2 pagination/search problems
- Problem solving
  - Core: Pagination, search, filtering
  - Stretch: Complex queries with Q objects
- Deliverables
  - List view with working pagination, search, filters; URL state preserved

#### Day 4 (Thu): REST API with Django REST Framework
- Topics
  - DRF serializers and ModelSerializer
  - ViewSets and routers for URL configuration
  - Authentication for APIs (token/session)
  - API permissions; per-user filtering via get_queryset
- Hands-on
  - Install and configure DRF
  - Create TaskSerializer with validation (read-only: created_at, updated_at, owner)
  - Build TaskViewSet with full CRUD and router URLs
  - Restrict API to authenticated users; filter QuerySets by owner
  - Test with the browsable API, curl/Postman, and DRF APIClient
  - Solve 2-3 DRF problems from ProblemBank_Django.md
- Problem solving
  - Core: Serializer with validation, ViewSet with filtering
  - Stretch: Nested serializers, custom API actions
- Deliverables
  - Full CRUD API at /api/tasks/ with validation, per-user isolation, and API tests

#### Day 5 (Fri): Frontend Integration & Polish
- Topics
  - Consuming the REST API from JavaScript (fetch)
  - CSRF token handling
  - Client-side validation matching server rules
  - Simple state management; loading/error/empty states
  - UX polish: responsive design, accessibility basics
- Hands-on
  - Build static frontend (index.html, styles.css, js/api.js, js/ui.js, js/app.js)
  - Implement full CRUD through the API with error handling
  - Add client-side validation and inline error display
  - Handle loading/error/empty states; polish responsiveness
  - Complete manual E2E testing checklist
- Problem solving
  - Core: API client with error and CSRF handling
  - Stretch: Optimistic updates, keyboard shortcuts
- Deliverables
  - Working SPA consuming the Django API; E2E checklist completed; screenshots

### Weekend assignment
**Complete Full-Stack Django Application**

Build a fully-featured Task Tracker with auth, REST API, and frontend:

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
5. **API**:
   - RESTful endpoints for tasks (DRF)
   - Authentication (session/token)
   - Proper HTTP status codes
6. **Frontend**:
   - Static frontend consuming the API (CRUD via fetch)
   - Client-side validation and loading/error/empty states
   - CSRF handling; responsive design
7. **Testing**:
   - >85% coverage
   - Unit tests for models, views, forms
   - Integration tests for user flows
   - API tests
8. **Documentation**:
   - Comprehensive README
   - API documentation
   - Architecture diagram
   - Screenshots/demo GIF
9. **Production Prep (Optional stretch)**:
   - Environment variables for secrets
   - DEBUG=False configuration
   - Static files collected
   - Basic security headers

**Acceptance criteria:**
- All features functional and tested
- 10+ advanced Django problems solved from ProblemBank
- Authentication working with proper isolation
- Pagination, search, filtering working
- Test coverage >85%
- Frontend integrated with the API (CRUD end-to-end)
- Documentation comprehensive
- Code quality tools pass

### Suggested problems (10-14 total for the week)
- See `intern_training/ProblemBank_Django.md` - focus on auth, API, and testing sections
- Daily quota: 2-3 problems (focus on advanced patterns)

### Final promotion gate (program completion)
- Complete full-stack Django application (auth, API, frontend)
- 10+ advanced Django problems solved
- All features functional with comprehensive tests
- Complete documentation
- Weekend assignment meets all criteria
- Ready for team integration on Day 1




