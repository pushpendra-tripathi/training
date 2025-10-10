## Week 3 · Day 5 — Binary Trees & BST Mastery

### Objectives
- Master binary tree structure, properties, and traversals
- Understand Binary Search Tree (BST) operations
- Practice both recursive and iterative solutions
- Learn DFS vs. BFS patterns

### Tasks
1) **Binary Tree Node Structure**
   - Define TreeNode class: value, left, right
   - Understand tree terminology: root, leaf, parent, child, height, depth
   - Tree properties: complete, full, perfect, balanced

2) **Binary Tree Traversals (DFS)**
   - **Inorder** (Left → Root → Right): For BST, gives sorted order
     - Implement: recursive AND iterative (stack)
   - **Preorder** (Root → Left → Right): For tree cloning/serialization
     - Implement: recursive AND iterative (stack)
   - **Postorder** (Left → Right → Root): For tree deletion
     - Implement: recursive AND iterative (stack, harder)
   - Pattern: Recursive is natural, iterative uses explicit stack

3) **Binary Tree Traversal (BFS)**
   - **Level Order Traversal**: Visit level by level
   - Implementation: Queue-based
   - Use cases: Shortest path, level-specific operations
   - Pattern: BFS uses queue, DFS uses stack (or recursion)

4) **Binary Search Tree (BST)**
   - Property: left < root < right (recursively)
   - Operations:
     - **Search**: O(h) time, navigate left/right
     - **Insert**: O(h) time, find position and insert
     - **Delete**: O(h) time, three cases (leaf, one child, two children)
     - **Validate**: Check BST property with valid ranges
   - Common problems:
     - Kth smallest: inorder traversal
     - Lowest Common Ancestor: Use BST property

5) **Tree Properties & Algorithms**
   - **Height/Depth**: Recursive calculation
   - **Balanced**: Check if height-balanced (AVL property)
   - **Symmetric**: Mirror image check
   - **Diameter**: Longest path between any two nodes
   - **Invert**: Swap left and right children

6) **DFS vs. BFS Decision Guide**
   - **Use DFS when**:
     - Need to explore all paths
     - Tree traversal (inorder, preorder, postorder)
     - Backtracking problems
   - **Use BFS when**:
     - Need shortest path
     - Level-by-level processing
     - Minimum depth problems

7) **Graph Basics (Introduction)**
   - Representation: adjacency list vs. adjacency matrix
   - Tree is special graph: connected, acyclic, N nodes → N-1 edges
   - Graph traversal: DFS and BFS with visited tracking

8) Problem solving (7-9 problems from ProblemBank_DSA.md - Trees section)
   - **Core (must solve)**:
     - Binary Tree Inorder Traversal (recursive + iterative)
     - Binary Tree Preorder Traversal (recursive + iterative)
     - Binary Tree Level Order Traversal (BFS)
     - Maximum Depth of Binary Tree
     - Validate Binary Search Tree
   - **Stretch**:
     - Invert Binary Tree
     - Symmetric Tree
     - Lowest Common Ancestor of BST
     - Insert into BST
   - **Challenge**:
     - Diameter of Binary Tree
     - Balanced Binary Tree
     - Kth Smallest Element in BST (bonus)

### Problem solving (60–90 min)
- From ProblemBank_DSA.md: Trees & BST section (problems 29-44)
- Focus on both recursive and iterative solutions

### Outcomes
- Master all binary tree traversals (recursive + iterative)
- Understand BST operations and properties
- Recognize when to use DFS vs. BFS
- Build strong recursion skills

### Deliverables
- **TreeNode class** with proper structure
- **Tree traversal implementations**:
  - Inorder (recursive + iterative with stack)
  - Preorder (recursive + iterative with stack)
  - Postorder (recursive + iterative with stack)
  - Level Order (BFS with queue)
- **BST operations**:
  - Insert, search, validate
  - At least one implemented with tests
- **7-9 tree problems solved** with:
  - Type hints
  - Docstrings with complexity analysis
  - Both recursive and iterative (where applicable)
  - Comprehensive tests with edge cases:
    - Empty tree (None)
    - Single node
    - Skewed tree (all left or all right)
    - Balanced tree
    - Complete binary tree
- **Pattern guide document** (`tree_patterns.md`):
  - When to use each traversal
  - DFS vs. BFS decision tree
  - Recursive vs. iterative tradeoffs
  - Common BST patterns
  - Visual examples

### Submission checklist
- [ ] TreeNode class defined
- [ ] All 4 traversals implemented (inorder, preorder, postorder, level order)
- [ ] At least 2 traversals have both recursive and iterative versions
- [ ] 7+ tree/BST problems solved
- [ ] BST validation working correctly
- [ ] DFS vs. BFS pattern guide created
- [ ] Tests cover edge cases (empty, single, skewed, balanced)
- [ ] Complexity documented for all solutions
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


