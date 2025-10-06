## Week 3 — Auth, Forms, Validation, Simple APIs, Testing Basics

### Weekly learning goals
- Add authentication and per-user data access.
- Strengthen forms, validation, and messages.
- Expose a small REST API (using Django REST Framework) without overwhelming depth.
- Learn testing basics and how to verify functionality locally.

### Daily schedule

#### Day 1 (Mon): Auth and permissions
- Topics
  - Django auth (login, logout, signup), user model basics; messages framework.
  - Per-user filtering to ensure privacy; authorization checks in views.
- Hands-on
  - Add login/logout views; restrict task listing to the logged-in user; owner on `Task` model.
- Problem solving (45–60 min)
  - From LeetCode: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
- Deliverables
  - Authenticated flows working; unauthorized access blocked.

#### Day 2 (Tue): Forms and validation
- Topics
  - `ModelForm`, custom `clean_` methods, field validators, error messages.
  - UX: sticky forms, success/failure banners.
- Hands-on
  - Add server-side validation to `Task` creation/update; improve error display in templates.
- Problem solving
  - From LeetCode: [Min Stack](https://leetcode.com/problems/min-stack/)
  - From Euler: [Problem 5](https://projecteuler.net/problem=5)
- Deliverables
  - Robust forms with clear validation and messages.

#### Day 3 (Wed): Simple API with DRF
- Topics
  - DRF basics: serializers, viewsets, routers; browsable API.
- Hands-on
-  - Install DRF and expose `/api/tasks/` with list/create/retrieve/update/delete scoped to the current user.
  - Add simple serializer validation (e.g., title length, due_date must be in the future).
- Problem solving
  - From LeetCode: [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
  - From LeetCode: [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- Deliverables
  - API tested with HTTPie/Postman; correct status codes and error shapes.

#### Day 4 (Thu): Testing basics
- Topics
  - Unit tests for models, views, forms, and API endpoints; fixtures; using Django test client.
- Hands-on
  - Write a small set of tests that cover: creating tasks, permission checks, and one API endpoint.
  - Add a `Makefile test` target to run tests locally.
- Problem solving
  - From LeetCode: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
  - From LeetCode: [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- Deliverables
  - Tests pass locally; basic coverage of critical paths.

#### Day 5 (Fri): Performance and pagination basics
- Topics
  - Pagination defaults, basic query optimization (select_related/prefetch_related intro).
- Hands-on
  - Ensure list views and API endpoints are paginated; measure simple before/after queries in shell.
- Problem solving
  - From LeetCode: [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
  - From Euler: [Problem 6](https://projecteuler.net/problem=6)
- Deliverables
  - Paginated endpoints and pages; simple notes on observed query counts.

### Weekend assignment
API-first extension of Task Tracker:
- Add filtering parameters to `/api/tasks/` (e.g., status, due_date range) and document them in the project README.
- Write tests for one success and one failure case per endpoint.
- Ensure the project is easy to set up and run locally with a short, clear README.
- Quality gate: `black`, `isort`, `pylint` all pass locally.


