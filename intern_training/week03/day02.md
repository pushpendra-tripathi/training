## Week 3 · Day 2 — Stacks & Queues

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
Stack and Queue implementations from scratch, plus solutions to 5-7 problems using monotonic stack and queue patterns.

**Why does this matter for Django?**  
Django's middleware stack, task queues (Celery), and request/response cycle use stack/queue patterns. Understanding these data structures helps you debug middleware ordering and async task processing.

**What does success look like?**  
- Stack and Queue with O(1) operations implemented correctly
- Can recognize monotonic stack pattern (e.g., next greater element)
- All implementations include comprehensive tests

---

### Objectives
- Understand LIFO (stack) and FIFO (queue) data structures
- Implement stacks and queues from scratch
- Apply to real problems: parentheses matching, monotonic stack patterns

### Tasks
1) Stack implementation
   - Build stack using Python list
   - Operations: push, pop, peek, isEmpty - all O(1)
   - Applications: function call stack, undo/redo, DFS

2) Queue implementation
   - Build queue using collections.deque or two stacks
   - Operations: enqueue, dequeue, peek - all O(1) amortized
   - Applications: BFS, task scheduling

3) Advanced patterns
   - Monotonic stack: daily temperatures, next greater element
   - Implement queue using two stacks

4) Problem solving (5-7 problems from ProblemBank_DSA.md)
   - **Core (must solve)**:
     - Valid Parentheses
     - Min Stack
     - Implement Queue using Stacks
   - **Stretch**:
     - Daily Temperatures
     - Evaluate Reverse Polish Notation
   - **Challenge**:
     - Largest Rectangle in Histogram (bonus)

### Problem solving
- From ProblemBank_DSA.md: Stacks & Queues section
- Focus on pattern recognition

### Outcomes
- Recognize when to use stack vs. queue
- Understand monotonic stack pattern
- Implement with proper time complexity

### Deliverables
- Stack and Queue implementations with comprehensive tests
- 5-7 problems solved with:
  - Type hints
  - Complexity analysis
  - Pattern identification in comments
- Tests covering edge cases (empty, single element, overflow scenarios)

### Submission checklist
- [ ] Stack implementation with tests
- [ ] Queue implementation with tests
- [ ] 5+ stack/queue problems solved
- [ ] Monotonic stack pattern documented
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


