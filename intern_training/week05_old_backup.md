## Week 5 (Bonus) — Django Polish + Auth + API (+ optional frontend)
### Prerequisite (promotion from Week 4)
- Proceed only if Week 4 promotion gate is met (CRUD + forms + list features + admin action + tests passing).

### Weekly learning goals
- Add auth basics and per-user filtering; strengthen validation and messages.
- Introduce a simple REST API (DRF optional) scoped to the user.
- Optionally wire a small static frontend consuming the API.

### Daily schedule

#### Day 1 (Mon): Auth and permissions
- Topics
  - Django auth (login, logout, signup), messages; per-user filtering.
- Hands-on
  - Add login/logout; restrict list to owner; set owner on model where relevant.
- Deliverables
  - Authenticated flows working; unauthorized access blocked.

#### Day 2 (Tue): Forms and validation polish
- Topics
  - ModelForm custom validation and clean UX messages.
- Hands-on
  - Add server-side validation; improve error display in templates.
- Deliverables
  - Robust forms with clear validation and messages.

#### Day 3 (Wed): Simple API (DRF optional)
- Topics
  - Serializers, viewsets, routers (if using DRF); simple JSON views if not.
- Hands-on
  - Expose `/api/tasks/` with list/create/retrieve/update/delete scoped to current user.
- Deliverables
  - API tested with HTTPie/Postman; correct status codes and error shapes.

#### Day 4 (Thu): Pagination/search and small performance wins
- Topics
  - Paginated endpoints; basic select_related/prefetch_related awareness.
- Hands-on
  - Ensure paginated list endpoints; note simple query counts before/after.
- Deliverables
  - Paginated endpoints; short notes on observed query counts.

#### Day 5 (Fri): Docs and optional frontend wiring
- Topics
  - Document API usage and optional static frontend consumption.
- Hands-on
  - If desired, use `frontend_template/` to render `/api/tasks/` results.
- Deliverables
  - README section: how to run auth + API (and optional frontend); screenshots.

### Weekend assignment — API-first enhancement
- Add filtering parameters to `/api/tasks/` (e.g., status, due_date range) and document them.
- Write tests for one success and one failure case per endpoint.
- Ensure the project is easy to set up and run locally with a short, clear README.
- Quality gate: `black`, `isort`, `pylint` all pass locally.

