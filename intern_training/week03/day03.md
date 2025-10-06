## Week 3 · Day 3 — Simple REST API with DRF

### Objectives
- Expose a minimal REST API for tasks with authentication.

### Tasks
1) DRF setup
   - Install Django REST Framework and add it to `INSTALLED_APPS`
   - Create a serializer for the `Task` model that includes all necessary fields
   - Create a viewset for the `Task` model to handle CRUD operations
   - Configure serializer validation rules:
     - Title should be required and non-empty
     - Due date (if provided) must be in the future
     - Status must be a valid choice

2) Routing and scoping
   - Set up DRF router and register your Task viewset
   - Configure API URLs under `/api/` prefix
   - Implement per-user scoping: users should only see their own tasks
   - Ensure all API operations respect task ownership

3) Authentication and permissions
   - Configure authentication (session or token-based)
   - Set appropriate permission classes
   - Test that unauthenticated requests are rejected
   - Test that users cannot access others' tasks

### Problem solving (45–60 min)
- LeetCode: [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- LeetCode: [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

### Outcomes
- API endpoints for list/create/retrieve/update/delete with correct status codes.

### Deliverables
- Brief API notes in README; example curl/HTTPie commands.

### Submission checklist
- [ ] Endpoints work and are user-scoped
- [ ] Validation errors return clear messages
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


