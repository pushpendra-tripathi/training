## Week 6 · Weekend — Complete Full-Stack Django Application

### Overview
Build a fully-featured Task Tracker that brings together everything from Weeks 5-6: authentication, a REST API, and a frontend that consumes it.

### Requirements

#### 1. Authentication
- User registration, login, logout
- Password reset (email simulation via console backend)
- Per-user task isolation (owner ForeignKey, filtered querysets)

#### 2. Features (Views)
- Full CRUD with ownership checks (only the owner can view/edit/delete their tasks)
- Pagination (10 per page)
- Search by title/description
- Filters: status, priority, date range
- Bulk actions (mark multiple as done)

#### 3. Forms
- Robust validation with clear error messages
- Inline validation feedback
- Success/error messages throughout

#### 4. Admin
- Fully configured: list_display, list_filter, search_fields
- Custom actions (bulk status change)
- Inline editing where applicable

#### 5. API (Django REST Framework)
- RESTful endpoints for tasks at `/api/tasks/`
- Session or token authentication
- Per-user filtering via `get_queryset`
- Proper HTTP status codes

#### 6. Frontend
- Static frontend consuming the API (CRUD via fetch), built on `frontend_template/`
- Client-side validation matching server rules
- Loading/error/empty states
- CSRF token handling; responsive layout

#### 7. Testing (>85% coverage)
- Unit tests for models, views, forms
- Integration tests for full user flows (register → create task → edit → delete)
- API tests with DRF's `APIClient` (including cross-user isolation)

#### 8. Documentation
- Comprehensive README (setup, usage, screenshots/demo GIF)
- API documentation (endpoints, auth, example requests/responses)
- Architecture diagram (how auth, API, and frontend fit together)

#### 9. Production Prep (Optional stretch)
- Environment variables for secrets
- `DEBUG=False` configuration
- Static files collected
- Basic security headers

### Suggested Structure
```
week06/
  weekend/
    README.md
    ARCHITECTURE.md
    tasktracker/              # Django project (continues from Week 5)
      settings.py
      urls.py
    tasks/
      models.py                # Task model with owner FK
      views.py                 # Auth-aware CBVs
      forms.py
      admin.py
      urls.py
      serializers.py           # DRF serializers
      api_views.py             # DRF ViewSets
      api_urls.py
      tests/
        test_models.py
        test_views.py
        test_forms.py
        test_api.py
        test_integration.py    # Full user-flow tests
    frontend/                  # Based on frontend_template/
      index.html
      styles.css
      js/
        api.js
        ui.js
        app.js
    manage.py
    db.sqlite3 (gitignored)
```

### Acceptance Criteria
- [ ] **Authentication**: Registration, login, logout, password reset working
- [ ] **CRUD**: Full CRUD with per-user ownership enforced
- [ ] **Pagination/Search/Filtering**: All working together with preserved URL state
- [ ] **Forms**: Validation with clear error display
- [ ] **Admin**: Customized with a working custom action
- [ ] **API**: Full CRUD at `/api/tasks/` with per-user isolation and correct status codes
- [ ] **Frontend**: SPA consuming the API end-to-end (create/read/update/delete)
- [ ] **Testing**: >85% coverage; unit + integration + API tests all passing
- [ ] **Documentation**: README, API docs, and architecture diagram complete
- [ ] **Code Quality**: Passes `black`, `isort`, `pylint`
- [ ] **Problem Solving**: 10+ advanced Django problems solved from ProblemBank_Django.md

### Promotion Gate
To complete the program, you must:
- ✅ Meet all acceptance criteria above
- ✅ Application fully functional end-to-end (auth → API → frontend)
- ✅ Test coverage >85%
- ✅ 10+ advanced Django problems solved
- ✅ Documentation complete
- ✅ Code quality tools pass

### Tips
- Build on your Week 5 Task Tracker rather than starting over
- Get auth and per-user isolation solid before layering the API on top
- Test the API with curl/Postman before wiring up the frontend
- Keep the frontend simple — correctness and clear states matter more than polish
- Write integration tests for the flows that matter most (a user managing only their own tasks)
