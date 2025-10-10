## Week 6 · Day 5 — Frontend Integration & Polish

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A complete frontend SPA consuming the Django REST API, with CRUD operations, client-side validation, error handling, and polished UX.

**Why does this matter for Django?**  
Modern Django apps often use separate frontends. Understanding API consumption, CSRF handling, state management, and frontend-backend integration is essential for full-stack development.

**What does success look like?**  
- All CRUD operations working through the frontend
- CSRF tokens handled correctly
- Loading/error/empty states providing clear feedback

---

### Objectives
- Build frontend consuming Django API
- Add client-side validation and UX polish
- Implement complete E2E flow

### Tasks
1) Static Frontend Setup
   - Use provided `frontend_template/` as base
   - Serve with Django static files or separate server
   - Structure: index.html, app.js, api.js, ui.js, styles.css

2) API Client (api.js)
   - Fetch tasks: GET /api/tasks/
   - Create task: POST /api/tasks/
   - Update task: PUT /api/tasks/<id>/
   - Delete task: DELETE /api/tasks/<id>/
   - Error handling for all calls
   - CSRF token handling

3) UI Components (ui.js)
   - Render task list
   - Task card component
   - Create/edit form modal
   - Delete confirmation
   - Loading states
   - Error states
   - Empty states

4) State Management
   - Simple state object for tasks
   - Render on state changes
   - Optimistic updates (optional)

5) Client-Side Validation
   - Required fields
   - Date validation
   - Match server validation rules
   - Display inline errors

6) UX Polish
   - Responsive design
   - Keyboard shortcuts (optional)
   - Transitions/animations (subtle)
   - Focus management
   - Accessibility basics (ARIA labels)

7) E2E Testing
   - Manual testing checklist
   - All CRUD operations through UI
   - Error scenarios

### Outcomes
- Functional SPA consuming Django API
- Polished UX
- Complete integration of backend + frontend

### Deliverables
- Static frontend with:
  - Task list rendering
  - Create/edit/delete via modals
  - Client-side validation
  - Error handling
  - Loading/error/empty states
  - CSRF handling
  - Responsive design
- E2E testing checklist completed
- Screenshots of working app

### Submission checklist
- [ ] Frontend renders tasks from API
- [ ] CRUD operations functional
- [ ] Client-side validation working
- [ ] Error handling in place
- [ ] CSRF tokens handled
- [ ] E2E checklist completed
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them




