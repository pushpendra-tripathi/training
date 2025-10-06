## Week 3 · Day 1 — Auth and Per-User Data

### Objectives
- Add login/logout; ensure users only see their own tasks.

### Tasks
1) Auth flows
   - Enable Django auth views (login/logout); add templates.
2) Ownership
   - Add `owner` ForeignKey on `Task`; set owner on create; filter queries by request.user.
3) Access control
   - Block access to others’ tasks; add friendly messages and redirects.

### Problem solving (45–60 min)
- LeetCode: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

### Outcomes
- Authenticated app with per-user visibility.

### Deliverables
- Screens showing login and user-scoped task list; README notes on auth.

### Submission checklist
- [ ] Owner set on create; queries filtered by user
- [ ] Unauthorized access blocked
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


