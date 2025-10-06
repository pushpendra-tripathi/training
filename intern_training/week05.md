## Week 5 (Bonus) — Fullstack Integration: Django API + Frontend
### Prerequisite (promotion from Week 4)
- Proceed only if Week 4 promotion gate is met (templates DRY + list/search/pagination/sorting + admin action + tests passing).

### Weekly learning goals
- Build a small frontend that consumes your Django API.
- Implement end-to-end flows: login, list, detail, create/update via API.
- Keep backend code clean with local `black`, `isort`, and `pylint`.

### Daily schedule

#### Day 1 (Mon): Frontend scaffold + API consumption
- Topics
  - Static site scaffold (HTML/CSS/JS), fetch API basics, error handling.
- Hands-on
  - Start from `frontend_template/` and wire a page that fetches `/api/tasks/` and renders a list.
  - Add a simple filter UI (status) and client-side pagination.
- Problem solving (45–60 min)
  - From LeetCode: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (revisit with stack variations)
  - From Euler: [Problem 7](https://projecteuler.net/problem=7)
- Deliverables
  - Static page showing tasks from your local API, with loading/error states.

#### Day 2 (Tue): Auth integration and secure calls
- Topics
  - Session auth vs token auth in a simple local setup; CSRF for POST/PUT/DELETE.
- Hands-on
  - Implement login/logout UI and ensure API calls include CSRF token where needed.
  - Restrict display to user-owned tasks; show a friendly message when unauthenticated.
- Problem solving
  - From LeetCode: [Detect Capital](https://leetcode.com/problems/detect-capital/), [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- Deliverables
  - Authenticated fetch flow; protected actions require login.

#### Day 3 (Wed): Create/Update flows and form UX
- Topics
  - Frontend forms, client-side validation, handling server validation errors.
- Hands-on
  - Add a Create Task form and an Edit flow (modal or separate page) calling the API.
  - Show field-level errors returned by the API.
- Problem solving
  - From LeetCode: [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/), Euler: [Problem 8](https://projecteuler.net/problem=8)
- Deliverables
  - Create/Update forms working against the API; clear success/error states.

#### Day 4 (Thu): UI polish and state management
- Topics
  - Organizing JS modules, minimal state management, UX improvements (loading skeletons, toasts).
- Hands-on
  - Add filtering, sorting, and improved empty-state UX.
  - Refactor JS into modules: `api.js`, `state.js`, `ui.js`.
- Problem solving
  - From LeetCode: [3Sum](https://leetcode.com/problems/3sum/), [LRU Cache](https://leetcode.com/problems/lru-cache/)
- Deliverables
  - Cleaner structure and noticeably improved UX.

#### Day 5 (Fri): E2E sanity and docs
- Topics
  - Manual E2E test plan, documenting API usage from the frontend.
- Hands-on
  - Create a short checklist to verify login → list → create → edit → logout flows.
  - Document setup steps for both backend and frontend.
- Problem solving
  - From LeetCode: [Coin Change](https://leetcode.com/problems/coin-change/)
- Deliverables
  - README section: “How to run the fullstack demo”; screenshots or GIF.

### Weekend assignment — Fullstack mini demo
- Build a small front-end page for task details with a comments section (read-only or simple create), backed by a new `/api/tasks/<id>/comments/` endpoint.
- Include loading, error, and empty states; document how to run both backend and frontend.
- Ensure backend code passes `black`, `isort`, `pylint` locally.

### Quality reminders (daily)
- Before submitting each day: run `black .`, `isort .`, and `pylint **/*.py` on backend code.

