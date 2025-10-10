## Week 3 · Day 3 — Sorting & Searching

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
Binary search and merge sort implementations from scratch, plus 6-8 problems using search and sort algorithms.

**Why does this matter for Django?**  
Django querysets support ordering and filtering. Understanding sorting algorithms and binary search helps you optimize database queries with indexes and understand query performance.

**What does success look like?**  
- Bug-free binary search (iterative and recursive)
- Merge sort working correctly with O(n log n) time
- Can explain when to sort vs. use hash table

---

### Objectives
- Master binary search and its variations
- Understand sorting algorithms: merge sort, quick sort
- Analyze time/space complexity tradeoffs

### Tasks
1) Binary search mastery
   - Implement iterative and recursive binary search
   - Variations: find first/last occurrence, search in rotated array
   - When to apply: sorted arrays, optimization problems

2) Sorting algorithms
   - **Merge Sort**: divide-and-conquer, stable, O(n log n), O(n) space
   - **Quick Sort**: in-place, average O(n log n), worst O(n²)
   - Compare: when to use which

3) When to sort vs. other approaches
   - Sorting first vs. using hash table
   - Trade-offs: time vs. space

4) Problem solving (6-8 problems from ProblemBank_DSA.md)
   - **Core (must solve)**:
     - Binary Search
     - Merge Sorted Arrays
     - Merge Sort Implementation
   - **Stretch**:
     - Search in Rotated Sorted Array
     - Quick Select (Kth Largest Element)
     - Find First and Last Position in Sorted Array
   - **Challenge**:
     - Median of Two Sorted Arrays (bonus)

### Problem solving
- From ProblemBank_DSA.md: Sorting & Searching section
- Document algorithm choices and why

### Outcomes
- Implement binary search without bugs
- Understand merge sort and quick sort mechanics
- Choose appropriate algorithm for problem constraints

### Deliverables
- Binary search implementation (iterative + recursive) with tests
- Merge sort implementation with tests
- Quick sort implementation (optional)
- 6-8 problems solved with:
  - Type hints
  - Complexity analysis comparison (brute force vs. optimized)
  - Algorithm choice justification
- Complexity comparison table in README

### Submission checklist
- [ ] Binary search implemented correctly
- [ ] Merge sort working with tests
- [ ] 6+ sorting/searching problems solved
- [ ] Complexity comparisons documented
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


