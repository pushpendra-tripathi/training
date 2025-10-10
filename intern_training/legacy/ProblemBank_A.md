## Problem Bank A — Fundamentals (loops, collections, strings)

Format: Each problem lists an example input/output. Write small, pure functions with type hints and tests.

### Core (must)
1) Reverse a string
   - Input: "hello"
   - Output: "olleh"
   - Variants: iterative loop, slicing; note time O(n), space O(1)/O(n).
2) Top-K frequencies
   - Input: nums = [1,1,1,2,2,3], k = 2
   - Output: [1,2] (order arbitrary among ties)
3) Remove duplicates preserving order
   - Input: [3,1,3,2,1]
   - Output: [3,1,2]
4) Merge two sorted lists
   - Input: a=[1,3,5], b=[2,4,6]
   - Output: [1,2,3,4,5,6]
5) Validate parentheses with a stack
   - Input: "()[]{}"
   - Output: True
   - Input: "(]"
   - Output: False

### Stretch (nice)
6) First non-repeating character
   - Input: "swiss"
   - Output: "w" (or index 1, if you choose index)
7) Group anagrams
   - Input: ["eat","tea","tan","ate","nat","bat"]
   - Output: [["eat","tea","ate"],["tan","nat"],["bat"]] (order within groups not important)
8) Longest substring without repeating chars (sliding window)
   - Input: "abcabcbb"
   - Output: 3 ("abc")

### Challenge (bonus)
9) Container with most water (two pointers)
   - Input: [1,8,6,2,5,4,8,3,7]
   - Output: 49
10) LRU Cache (class design)
   - API: `get(key)->int`, `put(key,value)->None`, capacity n
   - Behavior: evict least-recently-used on overflow; O(1) ops with hashmap + doubly-linked list

### Guidance
- Prefer small, pure functions and early returns.
- Add tests for happy and edge cases; include big-O notes in docstrings.

