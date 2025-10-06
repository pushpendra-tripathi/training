## Week 5 · Day 2 — Auth Integration and Secure Calls

### Objectives
- Connect frontend to authenticated endpoints and handle CSRF for write actions.

### Tasks
1) Login/logout
   - Add a login UI; persist session; show logout.
2) CSRF handling
   - Obtain CSRF token and include it in POST/PUT/DELETE requests.
3) Protected views
   - Show tasks only for logged-in users; handle unauthenticated states.

### Problem solving (45–60 min)
- LeetCode: [Detect Capital](https://leetcode.com/problems/detect-capital/), [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

### Outcomes
- Secure authenticated calls; clear behavior across auth states.

### Deliverables
- Auth flow wired in UI and working against local backend.

### Submission checklist
- [ ] Auth-required API calls succeed; unauthenticated blocked with proper UI
- [ ] CSRF token included for writes
- [ ] README documents auth steps

