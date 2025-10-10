## Week 5 · Day 2 — Views & URL Routing

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
Complete CRUD views (list, detail, create, update, delete) using both FBVs and CBVs, with proper URL routing and named patterns.

**Why does this matter for Django?**  
Views are the core of Django applications. Understanding FBVs vs CBVs, URL routing, and the request/response cycle is fundamental to building any Django feature.

**What does success look like?**  
- All CRUD operations working through views
- URLs configured with named patterns and reverse() working
- Can explain when to use FBV vs CBV

---

### Objectives
- Build views using FBVs and CBVs
- Configure URL routing with named patterns
- Master the request/response cycle

### Tasks
1) Function-Based Views (FBVs)
   - Create list view for all tasks
   - Create detail view for single task
   - Understand request and response objects
   - Return HttpResponse, render(), redirect()

2) URL Configuration
   - App-level URLs: `tasks/urls.py`
   - Project-level URLs: include() app URLs
   - URL patterns with path()
   - Named URLs and reverse()
   - URL parameters: `<int:pk>`, `<slug:slug>`

3) Class-Based Views (CBVs)
   - ListView: display all tasks with pagination
   - DetailView: display single task
   - CreateView: form to create task
   - UpdateView: form to edit task
   - DeleteView: confirm and delete
   - Override get_queryset(), get_context_data()

4) Request/Response Cycle
   - Middleware flow
   - View processing
   - Template rendering
   - Context data

5) Problem solving (3-4 problems from ProblemBank_Django.md)
   - Core: FBV List view
   - Core: CBV ListView
   - Core: Detail View with slug
   - Stretch: Create View with validation
   - Stretch: Update and Delete Views

### Outcomes
- CRUD views functional
- URLs properly configured
- Understand FBV vs. CBV tradeoffs

### Deliverables
- All CRUD views implemented (list, detail, create, update, delete)
- URL routing with named patterns
- Views accessible at proper URLs
- 3-4 view problems solved

### Submission checklist
- [ ] List and Detail views working
- [ ] Create, Update, Delete views working
- [ ] URLs configured with names
- [ ] reverse() used in code
- [ ] 3+ view problems solved
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


