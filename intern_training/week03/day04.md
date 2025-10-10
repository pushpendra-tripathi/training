## Week 3 · Day 4 — Two Pointers & Sliding Window

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
Solutions to 6-8 problems using two-pointer and sliding window techniques, optimizing from O(n²) to O(n).

**Why does this matter for Django?**  
Django QuerySets can be inefficient if not optimized. Understanding algorithmic optimization (O(n²) → O(n)) helps you identify and fix slow queries, especially with `select_related` and `prefetch_related`.

**What does success look like?**  
- Can identify when to use two pointers vs. sliding window
- Have a reusable sliding window template
- All solutions show before/after complexity analysis

---

### Objectives
- Master two-pointer technique for array problems
- Understand sliding window pattern (fixed and variable size)
- Optimize O(n²) solutions to O(n)

### Tasks
1) Two-pointer technique
   - Pattern: when and why it works
   - Common scenarios: sorted arrays, palindromes, container problems
   - Time complexity: reducing nested loops to single pass

2) Sliding window pattern
   - Fixed-size window: max sum of k elements
   - Variable-size window: longest substring without repeating chars
   - Template: expand → check condition → contract

3) Problem solving (6-8 problems from ProblemBank_DSA.md)
   - **Core (must solve)**:
     - Valid Palindrome
     - Container With Most Water
     - Maximum Subarray (Kadane's)
   - **Stretch**:
     - 3Sum
     - Longest Substring Without Repeating Characters
     - Best Time to Buy and Sell Stock
   - **Challenge**:
     - Minimum Window Substring
     - Trapping Rain Water (bonus)

### Problem solving
- From ProblemBank_DSA.md: Two Pointers & Sliding Window sections
- Focus on pattern recognition and optimization

### Outcomes
- Recognize when to apply two pointers
- Implement sliding window efficiently
- Optimize brute-force O(n²) to O(n)

### Deliverables
- 6-8 problems solved with:
  - Brute force solution first (commented out)
  - Optimized solution with pattern explanation
  - Before/after complexity analysis
  - Type hints and tests
- Pattern guide document:
  - When to use two pointers
  - Sliding window template
  - Examples of each pattern

### Submission checklist
- [ ] 6+ two-pointer/sliding-window problems solved
- [ ] Pattern guide created
- [ ] Optimization documented (O(n²) → O(n))
- [ ] All solutions tested
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


