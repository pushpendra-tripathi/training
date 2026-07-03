## Week 3 — Data Structures & Algorithms

### Weekly learning goals
- Master fundamental data structures: arrays, hashmaps, stacks, queues
- Understand sorting and searching algorithms with complexity analysis
- Apply problem-solving patterns: two pointers, sliding window, recursion
- Build intuition for time/space complexity tradeoffs
- Develop systematic debugging and testing habits for algorithms

### Daily schedule

#### Day 1 (Mon): Arrays & Hash Tables
- Topics
  - Array operations, two-sum pattern, frequency counting
  - Hash tables: when to use, collision handling, time complexity
  - Common patterns: prefix sums, sliding window basics
- Hands-on
  - Implement hash table from scratch (simple version)
  - Solve 5-7 array/hashmap problems from ProblemBank_DSA.md
- Problem solving (from ProblemBank_DSA.md: Arrays & Strings, Hash Tables & Sets sections)
  - Core: Two Sum, Contains Duplicate, Valid Anagram
  - Stretch: Group Anagrams, First Non-Repeating Character, Intersection of Two Arrays
  - Challenge: Product of Array Except Self (bonus)
- Deliverables
  - Solutions with tests; complexity analysis in docstrings; patterns documented

#### Day 2 (Tue): Stacks & Queues
- Topics
  - Stack: LIFO, applications (parentheses, backtracking, DFS)
  - Queue: FIFO, applications (BFS, scheduling)
  - Monotonic stack/queue patterns
- Hands-on
  - Implement stack and queue using lists
  - Solve 5 stack/queue problems from ProblemBank_DSA.md (the full section)
- Problem solving (from ProblemBank_DSA.md: Stacks & Queues section)
  - Core: Valid Parentheses, Min Stack, Implement Queue using Stacks
  - Stretch: Daily Temperatures, Evaluate Reverse Polish Notation
  - Challenge: Largest Rectangle in Histogram (bonus, from the optional advanced section)
- Deliverables
  - Implementations with tests; problem solutions with complexity notes

#### Day 3 (Wed): Sorting & Searching
- Topics
  - Binary search and variations
  - Sorting algorithms: merge sort, quick sort
  - When to sort vs. when to use other approaches
- Hands-on
  - Implement binary search, merge sort from scratch
  - Solve 4-5 sorting/searching problems from ProblemBank_DSA.md (the section has 4, plus one cross-listed array problem)
- Problem solving (from ProblemBank_DSA.md: Sorting & Searching section, plus Merge Sorted Arrays from Arrays & Strings)
  - Core: Binary Search, Merge Sort Implementation, Merge Sorted Arrays
  - Stretch: Search in Rotated Sorted Array, Quick Select (Kth Largest Element)
- Deliverables
  - Algorithm implementations with tests; complexity comparisons documented

#### Day 4 (Thu): Two Pointers & Sliding Window
- Topics
  - Two-pointer technique: when and why it works
  - Sliding window: fixed and variable size
  - Time complexity optimization with these patterns
- Hands-on
  - Solve 6-8 two-pointer/sliding-window problems from ProblemBank_DSA.md
- Problem solving (from ProblemBank_DSA.md: Two Pointers & Sliding Window section, plus two cross-listed array problems)
  - Core: Valid Palindrome, Container With Most Water, Maximum Subarray (Kadane's)
  - Stretch: 3Sum, Longest Substring Without Repeating Characters, Best Time to Buy and Sell Stock
  - Challenge: Minimum Window Substring, Trapping Rain Water (bonus, from the optional advanced section)
- Deliverables
  - Solutions with pattern identification; before/after complexity analysis

#### Day 5 (Fri): Trees, Recursion & Graph Basics
- Topics
  - Binary tree basics: recursive inorder traversal; level-order (BFS) traversal
  - DFS vs BFS: when to use each
  - Graph representation: adjacency list/matrix
  - **Note**: Preorder/postorder and iterative traversals are optional advanced problems, not core to this day
- Hands-on
  - Implement inorder (recursive) and level-order (BFS) traversals
  - Solve 4-6 tree/graph problems from ProblemBank_DSA.md
- Problem solving (from ProblemBank_DSA.md: Trees & Recursion, Graphs sections)
  - Core: Binary Tree Inorder Traversal, Maximum Depth of Binary Tree, Validate Binary Search Tree, Invert Binary Tree
  - Stretch: Binary Tree Level Order Traversal (BFS), Number of Islands (DFS/BFS)
- Deliverables
  - Traversal implementations with tests; solutions with complexity analysis

### Weekend assignment
**Algorithm Portfolio Project**

Build a comprehensive algorithm library with:
1. **Implementations**: Stack, Queue, Binary Search, Merge Sort, Tree Traversals
2. **Tests**: Full pytest suite with edge cases for each algorithm
3. **Documentation**:
   - README with complexity analysis table
   - Docstrings with examples and Big-O notation
   - Pattern guide (when to use which algorithm/data structure)
4. **Problem Solutions**: At least 28 problems from ProblemBank_DSA.md with:
   - Multiple approaches (brute force → optimized)
   - Complexity analysis
   - Pattern identification
5. **Quality**: `black`, `isort`, `pylint` pass; type hints throughout

**Acceptance criteria:**
- All implementations tested and working
- 28+ DSA problems solved with tests
- Complexity documented for each solution
- Pattern guide clear and useful
- Code quality tools pass

### Suggested problems (25-35 total for the week)
- See `intern_training/ProblemBank_DSA.md` (Core/Stretch/Challenge)
- Daily quota varies by section size (4-8 per day) — see each day's plan above
- Focus on understanding patterns, not just solving

### Promotion gate (advance to Week 4 if all met)
- 28+ DSA problems solved with comprehensive tests
- Algorithm implementations correct and tested
- Complexity analysis documented and accurate
- Pattern recognition demonstrated
- Quality gates pass (`black`, `isort`, `pylint`)
- Weekend assignment complete with all acceptance criteria
