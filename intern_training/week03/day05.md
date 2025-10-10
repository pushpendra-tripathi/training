## Week 3 · Day 5 — Trees, Recursion & Graph Basics

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
Binary tree implementations with DFS/BFS traversals, BST validation, and 4-5 tree/recursion problems solved.

**Why does this matter for Django?**  
Django's template system and model relationships form tree structures. Understanding recursion and tree traversal helps you work with nested templates, hierarchical categories, and recursive queries.

**What does success look like?**  
- Comfortable writing recursive functions on trees
- Can choose between DFS and BFS appropriately
- BST validation working correctly

---

### Objectives
- Understand binary tree structure and recursive thinking
- Learn DFS vs. BFS traversal patterns
- Introduce Binary Search Trees (BST)
- Get first exposure to graph concepts

### Tasks
1) **Binary Tree Fundamentals**
   - TreeNode structure: value, left, right
   - Tree terminology: root, leaf, parent, child, height, depth
   - Why trees? Hierarchical data (file systems, DOM, categories)

2) **Recursion on Trees**
   - Natural fit: tree structure is inherently recursive
   - Base case: None or leaf node
   - Recursive case: process left and right subtrees
   - Example: Calculate depth recursively

3) **Tree Traversals**
   - **Inorder (DFS)**: Left → Root → Right
     - For BST, gives sorted order
     - Implement recursively
   - **Level Order (BFS)**: Level by level
     - Uses queue
     - Good for shortest path, level-specific operations

4) **Binary Search Tree (BST) Introduction**
   - Property: left < root < right (recursively)
   - Validate BST: Check property with valid ranges
   - Common operations: search, insert (conceptual understanding)

5) **DFS vs. BFS Decision Guide**
   - **Use DFS (recursion/stack) when**:
     - Exploring all paths
     - Tree traversal (inorder, preorder, postorder)
     - Simpler to implement recursively
   - **Use BFS (queue) when**:
     - Need shortest path
     - Level-by-level processing
     - Want to find something nearest to root

6) **Graph Basics (Conceptual)**
   - Tree is special graph: connected, acyclic
   - Graph representations: adjacency list vs. matrix
   - Graph traversal uses same DFS/BFS patterns
   - Visited tracking required (graphs can have cycles)

7) **Problem solving (4-5 problems from ProblemBank_DSA.md - Trees section)**
   - **Core (must solve 3-4)**:
     - Binary Tree Inorder Traversal (recursive)
     - Maximum Depth of Binary Tree
     - Validate Binary Search Tree
     - Invert Binary Tree (confidence builder)
   - **Stretch (if time allows 1-2)**:
     - Binary Tree Level Order Traversal (BFS)
     - Number of Islands (apply DFS/BFS to grid)

### Problem solving
- From ProblemBank_DSA.md: Trees & Recursion section (problems 29-35)
- **Focus**: Understanding recursion, not memorizing all tree problems
- **Goal**: Comfortable with recursive thinking, DFS/BFS patterns

### Outcomes
- Understand binary tree structure
- Comfortable writing recursive functions on trees
- Know when to use DFS vs. BFS
- Understand BST property
- Can apply DFS/BFS to graph-like problems

### Deliverables
- **TreeNode class** defined
- **Binary Tree Inorder Traversal** (recursive) implemented and tested
- **Maximum Depth** (recursive) implemented and tested
- **Validate BST** implemented and tested
- **4-5 tree/recursion problems solved** with:
  - Type hints
  - Docstrings with complexity analysis
  - Tests with edge cases:
    - Empty tree (None)
    - Single node
    - Left-skewed tree
    - Right-skewed tree
    - Balanced tree
- **Recursion notes** in `LEARNING.md`:
  - When recursion is appropriate
  - Base case vs. recursive case
  - DFS vs. BFS decision guide
  - Tree traversal patterns

### Submission checklist
- [ ] TreeNode class defined
- [ ] Inorder traversal (recursive) working
- [ ] Maximum depth (recursive) working
- [ ] Validate BST working correctly
- [ ] 4-5 tree/recursion problems solved
- [ ] Recursion patterns documented
- [ ] Tests cover edge cases
- [ ] Complexity documented for solutions
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them

### Notes
- **Don't stress about mastering all tree algorithms** - this is an introduction
- Focus on understanding **recursive thinking** - it's useful everywhere
- DFS/BFS patterns appear in many places (not just trees)
- Advanced tree problems (iterative traversals, complex BST operations) are **optional** - see end of ProblemBank_DSA.md
- For Django development, understanding hierarchical data concepts is sufficient


