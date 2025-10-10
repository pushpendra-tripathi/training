## Week 3 · Weekend — Algorithm Portfolio Project

### Overview
Build a comprehensive algorithm library demonstrating DSA mastery with implementations, tests, and documentation.

### Requirements

#### 1. Core Data Structure Implementations
Implement from scratch with full test coverage:
- **Stack** (using list)
  - Methods: push, pop, peek, is_empty, size
  - Tests: empty stack, single element, overflow
- **Queue** (using deque or two stacks)
  - Methods: enqueue, dequeue, peek, is_empty, size
  - Tests: empty queue, FIFO order verification
- **Binary Search Tree** (optional stretch)
  - Methods: insert, search, delete
  - Traversals: inorder, preorder, postorder

#### 2. Core Algorithm Implementations
Implement with comprehensive tests:
- **Binary Search** (iterative and recursive)
- **Merge Sort** (divide and conquer)
- **Quick Sort** (optional)
- **Tree Traversals** (DFS: inorder, preorder, postorder; BFS)

#### 3. Problem Solutions (Minimum 30 from ProblemBank_DSA.md)
Solve and document:
- **Arrays & Hash Tables**: 8+ problems
- **Stacks & Queues**: 6+ problems
- **Sorting & Searching**: 6+ problems
- **Two Pointers & Sliding Window**: 6+ problems
- **Trees & Graphs**: 4+ problems

Each solution must include:
- Multiple approaches (brute force → optimized)
- Complexity analysis (time and space)
- Type hints
- Comprehensive tests (happy path + edge cases)
- Pattern identification in comments

#### 4. Documentation
Create comprehensive README with:
- **Complexity Reference Table**:
  ```
  | Algorithm      | Time (Best) | Time (Avg) | Time (Worst) | Space |
  |----------------|-------------|------------|--------------|-------|
  | Binary Search  | O(1)        | O(log n)   | O(log n)     | O(1)  |
  | Merge Sort     | O(n log n)  | O(n log n) | O(n log n)   | O(n)  |
  | ...            |             |            |              |       |
  ```
- **Pattern Guide**:
  - When to use hash tables
  - Two-pointer technique scenarios
  - Sliding window template
  - DFS vs. BFS decision tree
- **Problem Index**: Organized by pattern
- **Setup Instructions**: How to run tests

#### 5. Testing
- pytest suite with >95% coverage
- Parametrized tests for variations
- Edge case coverage:
  - Empty inputs
  - Single element
  - Duplicates
  - Negative numbers
  - Large inputs (performance)

#### 6. Code Quality
- All code passes `black`, `isort`, `pylint`
- Type hints throughout
- Docstrings with:
  - Description
  - Args and return types
  - Complexity analysis
  - Examples

### Suggested Structure
```
week03/
  weekend/
    README.md                 # Main documentation
    algorithms/
      __init__.py
      search.py              # Binary search variants
      sort.py                # Merge sort, quick sort
      tree_traversal.py      # DFS, BFS
    data_structures/
      __init__.py
      stack.py
      queue.py
      bst.py (optional)
    problems/
      arrays_hash.py         # Array/hash table solutions
      stacks_queues.py       # Stack/queue solutions
      sort_search.py         # Sorting/searching solutions
      two_pointers.py        # Two-pointer solutions
      trees_graphs.py        # Tree/graph solutions
    tests/
      test_algorithms.py
      test_data_structures.py
      test_problems_arrays.py
      test_problems_stacks.py
      test_problems_sort.py
      test_problems_pointers.py
      test_problems_trees.py
    docs/
      PATTERNS.md            # Pattern guide
      COMPLEXITY.md          # Complexity reference
```

### Acceptance Criteria
- [ ] All core data structures implemented and tested
- [ ] All core algorithms implemented and tested
- [ ] **30+ problems** solved from ProblemBank_DSA.md
- [ ] Each solution has:
  - [ ] Multiple approaches (where applicable)
  - [ ] Complexity analysis
  - [ ] Comprehensive tests
  - [ ] Type hints and docstrings
- [ ] README with complexity table and pattern guide
- [ ] Test coverage >95%
- [ ] All code passes quality tools (`black`, `isort`, `pylint`)
- [ ] Pattern guide is clear and useful
- [ ] Examples demonstrate understanding

### Promotion Gate
To advance to Week 4, you must:
- ✅ Complete all acceptance criteria above
- ✅ Solve minimum 30 DSA problems with tests
- ✅ Document complexity for all implementations
- ✅ Demonstrate pattern mastery in pattern guide
- ✅ Achieve test coverage >95%
- ✅ Pass code quality gates

### Tips
- Start with Core problems from each section
- Work through patterns systematically
- Test as you go, don't save testing for last
- Document patterns as you recognize them
- Ask for help if stuck, but try brute force first
- Focus on understanding over speed


