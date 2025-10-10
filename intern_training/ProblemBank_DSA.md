## Problem Bank — Data Structures & Algorithms (35 problems)

**Target**: Week 3. Pick 6-8 problems daily; focus on patterns and complexity analysis.

**Problem Breakdown**:
- Arrays & Strings: 6 problems
- Hash Tables & Sets: 4 problems
- Stacks & Queues: 5 problems
- Two Pointers & Sliding Window: 5 problems
- Sorting & Searching: 4 problems
- Linked Lists: 4 problems
- **Trees & Recursion: 5 problems (core introduction)**
- Graphs: 2 problems

**Note**: Advanced tree/graph problems moved to optional section at end if you want to challenge yourself.

### Core (must) — Arrays & Strings

1) **Two Sum**
   - Input: nums=[2,7,11,15], target=9
   - Output: [0,1] (indices of 2 and 7)
   - Complexity: O(n) with hashmap

2) **Best Time to Buy and Sell Stock**
   - Input: prices=[7,1,5,3,6,4]
   - Output: 5 (buy at 1, sell at 6)
   - One-pass solution

3) **Contains Duplicate**
   - Input: [1,2,3,1]
   - Output: True
   - Use set for O(n) time

4) **Product of Array Except Self**
   - Input: [1,2,3,4]
   - Output: [24,12,8,6]
   - Without division, O(n)

5) **Maximum Subarray (Kadane's Algorithm)**
   - Input: [-2,1,-3,4,-1,2,1,-5,4]
   - Output: 6 (subarray [4,-1,2,1])

6) **Merge Sorted Arrays**
   - Input: arr1=[1,3,5], arr2=[2,4,6]
   - Output: [1,2,3,4,5,6]
   - In-place variant for stretch

### Core (must) — Hash Tables & Sets

7) **Valid Anagram**
   - Input: s="anagram", t="nagaram"
   - Output: True
   - O(n) with frequency map

8) **Group Anagrams**
   - Input: ["eat","tea","tan","ate","nat","bat"]
   - Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

9) **First Non-Repeating Character**
   - Input: "leetcode"
   - Output: 'l' (or index 0)

10) **Intersection of Two Arrays**
    - Input: nums1=[1,2,2,1], nums2=[2,2]
    - Output: [2]
    - Unique elements only

### Stretch (nice) — Stacks & Queues

11) **Valid Parentheses**
    - Input: "()[]{}"
    - Output: True
    - Input: "(]"
    - Output: False
    - Use stack

12) **Min Stack**
    - Methods: push, pop, top, getMin (all O(1))
    - Implementation: use auxiliary stack

13) **Implement Queue using Stacks**
    - Methods: enqueue, dequeue, peek
    - Amortized O(1)

14) **Daily Temperatures**
    - Input: [73,74,75,71,69,72,76,73]
    - Output: [1,1,4,2,1,1,0,0] (days until warmer)
    - Monotonic stack

15) **Evaluate Reverse Polish Notation**
    - Input: ["2","1","+","3","*"]
    - Output: 9 ((2+1)*3)

### Stretch (nice) — Two Pointers & Sliding Window

16) **Valid Palindrome**
    - Input: "A man, a plan, a canal: Panama"
    - Output: True
    - Ignore non-alphanumeric, case-insensitive

17) **Container With Most Water**
    - Input: [1,8,6,2,5,4,8,3,7]
    - Output: 49 (indices 1 and 8)
    - Two pointers

18) **3Sum**
    - Input: [-1,0,1,2,-1,-4]
    - Output: [[-1,-1,2],[-1,0,1]]
    - Avoid duplicates

19) **Longest Substring Without Repeating Characters**
    - Input: "abcabcbb"
    - Output: 3 ("abc")
    - Sliding window

20) **Minimum Window Substring**
    - Input: s="ADOBECODEBANC", t="ABC"
    - Output: "BANC"
    - Sliding window + hashmap

### Stretch (nice) — Sorting & Searching

21) **Binary Search**
    - Input: nums=[1,2,3,4,5,6,7], target=4
    - Output: 3 (index)
    - O(log n)

22) **Search in Rotated Sorted Array**
    - Input: [4,5,6,7,0,1,2], target=0
    - Output: 4
    - Modified binary search

23) **Merge Sort Implementation**
    - Input: [5,2,8,1,9]
    - Output: [1,2,5,8,9]
    - Divide and conquer

24) **Quick Select (Kth Largest Element)**
    - Input: [3,2,1,5,6,4], k=2
    - Output: 5 (2nd largest)
    - Average O(n)

### Challenge (bonus) — Linked Lists

25) **Reverse Linked List**
    - Iterative and recursive solutions
    - O(n) time, O(1) space for iterative

26) **Detect Cycle in Linked List**
    - Floyd's cycle detection (tortoise and hare)
    - Return: cycle start node

27) **Merge Two Sorted Lists**
    - Input: 1→2→4, 1→3→4
    - Output: 1→1→2→3→4→4
    - Recursive and iterative

28) **Remove Nth Node From End**
    - Input: 1→2→3→4→5, n=2
    - Output: 1→2→3→5
    - One-pass with two pointers

### Challenge (bonus) — Trees & Recursion (Core Introduction)

29) **Binary Tree Inorder Traversal**
    - Input: root = [1,null,2,3]
    - Output: [1,3,2] (left, root, right)
    - Implement: Recursive solution
    - Complexity: O(n) time, O(h) space
    - **Purpose**: Understand recursion on tree structures

30) **Maximum Depth of Binary Tree**
    - Input: root = [3,9,20,null,null,15,7]
    - Output: 3
    - Implement: Recursive DFS
    - Complexity: O(n) time, O(h) space
    - **Purpose**: Practice recursive tree thinking

31) **Binary Tree Level Order Traversal (BFS)**
    - Input: root = [3,9,20,null,null,15,7]
    - Output: [[3],[9,20],[15,7]]
    - Use: Queue for level-by-level traversal
    - Complexity: O(n) time, O(w) space (w = max width)
    - **Purpose**: Understand BFS pattern with queue

32) **Validate Binary Search Tree**
    - Input: root = [2,1,3]
    - Output: True
    - Input: root = [5,1,4,null,null,3,6]
    - Output: False (4's right child 3 < 4 but also < 5)
    - Method: Pass valid range down recursively
    - Complexity: O(n) time, O(h) space
    - **Purpose**: Understand BST property and range validation

33) **Invert Binary Tree**
    - Input: root = [4,2,7,1,3,6,9]
    - Output: [4,7,2,9,6,3,1]
    - Method: Swap left and right children recursively
    - Complexity: O(n) time, O(h) space
    - **Purpose**: Simple recursion practice, confidence builder

### Challenge (bonus) — Graphs (Introduction)

34) **Number of Islands (DFS/BFS)**
    - Input: grid = [["1","1","0"],["1","0","0"],["0","0","1"]]
    - Output: 2 (two islands)
    - Method: DFS or BFS to mark visited cells
    - Complexity: O(m×n) time, O(m×n) space
    - **Purpose**: Apply DFS/BFS to 2D grid, understand visited tracking

35) **Clone Graph**
    - Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    - Output: Deep copy of graph
    - Method: DFS/BFS with hashmap to track cloned nodes
    - Complexity: O(V+E) time and space
    - **Purpose**: Graph traversal with state tracking

### Guidance
- **Complexity analysis**: Document time and space for each solution
- **Multiple approaches**: Solve brute force first, then optimize
- **Edge cases**: Empty input, single element, duplicates, negative numbers
- **Patterns to master**:
  - Two pointers
  - Sliding window
  - Fast & slow pointers
  - Monotonic stack
  - Prefix sums
  - Binary search variants
  - DFS/BFS traversals
- **Testing**: Write pytest tests with multiple test cases
- **Type hints**: Use List, Optional, Tuple annotations
- **Docstrings**: Include complexity, algorithm name, and examples

---

## Advanced DSA Problems (Optional)

**Target**: Post-program or for those who finish early.

These problems are **NOT required** for the 6-week program but are excellent for:
- Deepening algorithm knowledge
- Competitive programming practice

### Advanced Trees & BST

36) **Binary Tree Preorder Traversal (Iterative)**
    - Implement using explicit stack (not recursion)
    - Complexity: O(n) time, O(h) space

37) **Binary Tree Postorder Traversal (Iterative)**
    - Hardest iterative traversal
    - Requires: two stacks or modified single stack approach

38) **Minimum Depth of Binary Tree**
    - BFS is optimal: O(n) time, finds answer when first leaf encountered
    - Compare with DFS approach

39) **Symmetric Tree**
    - Check if tree is mirror image of itself
    - Method: Recursive comparison of left/right subtrees

40) **Balanced Binary Tree**
    - Check if height-balanced (heights differ by at most 1)
    - Efficient: Return height + balanced flag in single pass

41) **Diameter of Binary Tree**
    - Longest path between any two nodes
    - Method: For each node, check left_height + right_height

42) **Lowest Common Ancestor of Binary Tree**
    - General binary tree (not BST, so can't use BST property)
    - Harder: requires recursive search in both subtrees

43) **Lowest Common Ancestor of BST**
    - Easier than general tree: use BST property to navigate
    - Can solve iteratively in O(1) space

44) **Insert into BST**
    - Maintain BST property after insertion
    - O(h) time

45) **Delete Node in BST**
    - Three cases: leaf, one child, two children
    - Most complex BST operation

46) **Kth Smallest Element in BST**
    - Use inorder traversal (gives sorted order for BST)
    - Can optimize with early stopping

47) **Serialize and Deserialize Binary Tree**
    - Convert tree to string and back
    - Important for tree storage/transmission

### Advanced Graphs

48) **Course Schedule (Cycle Detection)**
    - Topological sort or DFS cycle detection
    - Classic graph algorithm

49) **Course Schedule II (Topological Sort)**
    - Return ordering of courses
    - Classic topological sort application

50) **Pacific Atlantic Water Flow**
    - DFS/BFS from multiple start points
    - 2D grid graph problem

51) **Graph Valid Tree**
    - Check if graph is a valid tree
    - Conditions: connected + no cycles + n nodes → n-1 edges

52) **Shortest Path in Binary Matrix**
    - BFS for shortest path
    - 8-directional movement

### Advanced Patterns

53) **Trapping Rain Water** (Two Pointers + Stack)
    - Multiple approaches: brute force, DP, two pointers, stack
    - Classic interview problem

54) **Largest Rectangle in Histogram** (Monotonic Stack)
    - Advanced monotonic stack application
    - O(n) solution with stack

55) **Maximum Subarray Product** (DP)
    - Track both max and min (negatives flip)
    - Common interview question

56) **Longest Increasing Subsequence** (DP + Binary Search)
    - O(n²) DP solution
    - O(n log n) solution with binary search

**Note**: These problems are significantly harder than core problems. Attempt only after mastering the 35 core problems.


