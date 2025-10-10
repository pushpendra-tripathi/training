## Week 6 · Day 4 — Django REST Framework Basics

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A complete REST API for tasks using Django REST Framework, with serializers, ViewSets, and per-user authentication/filtering.

**Why does this matter for Django?**  
Modern Django applications often provide REST APIs. Understanding DRF serializers, ViewSets, and API authentication prepares you for building production APIs.

**What does success look like?**  
- Full CRUD API working via /api/tasks/
- Serializer validation matching model constraints
- Per-user filtering ensuring data isolation

---

### Objectives
- Build REST API with Django REST Framework (DRF)
- Create serializers for models
- Implement API views with ViewSets

### Tasks
1) DRF Setup
   - Install: `pip install djangorestframework`
   - Add to INSTALLED_APPS
   - Configure REST_FRAMEWORK settings
   - Add DRF URLs

2) Serializers
   - ModelSerializer for Task
   - Serialize all fields
   - Read-only fields: created_at, updated_at, owner
   - Validation in serializers
   - Nested serializers (Category)

3) ViewSets & Routers
   - TaskViewSet(viewsets.ModelViewSet)
   - Router for automatic URL routing
   - Endpoints: GET /api/tasks/, POST /api/tasks/, GET /api/tasks/<id>/, etc.
   - Override get_queryset for per-user filtering

4) Permissions
   - IsAuthenticated permission
   - Per-object permissions (optional)
   - Automatically set owner on create

5) Testing API
   - Use browser API (DRF browsable API)
   - Test with curl or Postman
   - Django test client for API tests
   - APIClient from DRF

6) Problem solving (2-3 problems from ProblemBank_Django.md)
   - Core: Serializer with validation
   - Core: ViewSet with filtering
   - Stretch: Nested serializers
   - Stretch: Custom API actions

### Outcomes
- REST API functional
- Per-user data isolation in API
- Understanding of DRF patterns

### Deliverables
- TaskSerializer with validation
- TaskViewSet with CRUD operations
- API URLs configured
- Per-user filtering in API
- API tests for major endpoints
- 2-3 DRF problems solved

### Submission checklist
- [ ] API endpoints working
- [ ] Serializer validation correct
- [ ] Per-user filtering in API
- [ ] API tests passing
- [ ] 2+ DRF problems solved
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them




