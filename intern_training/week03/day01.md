## Week 3 · Day 1 — Arrays & Hash Tables

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A hash table implementation from scratch and solutions to 5-7 array/hashmap problems using optimal patterns.

**Why does this matter for Django?**  
Django ORM querysets use hash-based lookups extensively. Understanding hash tables and O(1) lookups helps you write efficient database queries and avoid N+1 problems.

**What does success look like?**  
- Hash table with collision handling working correctly
- Can recognize two-sum and frequency counting patterns
- All solutions include time/space complexity analysis

---

### Objectives
- Master array operations and common patterns (two-sum, frequency counting, prefix sums)
- Understand hash table mechanics and when to use them
- Learn time/space complexity analysis

### Tasks
1) Array fundamentals
   - Implement from scratch: two-sum, contains duplicate, product of array except self
   - Understand: prefix sums, sliding window basics
   - Complexity: analyze time/space for each solution

2) Hash table deep dive
   - Build simple hash table with collision handling
   - Practice: frequency maps, set operations
   - Patterns: when hash table beats array sorting

3) Problem solving (5-7 problems from ProblemBank_DSA.md)
   - **Core (must solve)**:
     - Two Sum
     - Contains Duplicate
     - Valid Anagram
   - **Stretch**:
     - Group Anagrams
     - First Non-Repeating Character
     - Intersection of Two Arrays
   - **Challenge**:
     - Top K Frequent Elements (bonus)

### Problem solving
- From ProblemBank_DSA.md: Arrays & Hash Tables section
- Document patterns observed

### Outcomes
- Understand when to use hash tables vs. sorting
- Recognize two-sum and frequency counting patterns
- Analyze time/space complexity accurately

### Deliverables
- 5-7 problems solved with tests
- Solutions include:
  - Type hints
  - Docstrings with complexity analysis
  - Test cases covering edge cases
- Pattern notes in `LEARNING.md`

### Submission checklist
- [ ] Hash table implementation with tests
- [ ] 5+ array/hashmap problems solved
- [ ] Complexity documented for each solution
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


