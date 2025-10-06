## Week 2 · Day 1 — OOP and Packaging

### Objectives
- Use classes and dataclasses effectively; prefer composition; write clear `__repr__` and equality.
- Organize Python packages with clear public APIs and boundaries.

### Tasks
1) OOP fundamentals (from scratch)
   - **Basic classes**
     - Define a simple `Person` class with `__init__`, attributes, and methods
     - Instance vs class attributes
     - `self` keyword and instance methods
   - **Special methods (dunder methods)**
     - `__init__`: constructor
     - `__repr__` and `__str__`: string representations
     - `__eq__`: equality comparison
   - **Encapsulation**
     - Public vs "private" (underscore convention) attributes
     - `@property` decorator for computed attributes and getters/setters
   - **Inheritance**
     - Create base `Task` class and inherit `UrgentTask` subclass
     - Method overriding and `super()`
     - When to use inheritance vs composition
   - **Composition over inheritance**
     - Example: `TaskManager` that contains a list of `Task` objects
   - **Dataclasses** (after understanding basic classes)
     - Convert `Task` to a dataclass with validation in `__post_init__`
     - Fields: `title: str`, `description: str`, `status: Literal["todo","in_progress","done"]`, `due_date: date | None`
     - Invariants: `title` non-empty; if `due_date` present, must be >= today
     - Add status transition methods with validation
2) Packaging and modules
   - Restructure Week 1 utilities into `core/` and `features/` packages.
   - Provide `__all__` exports for public APIs; add minimal module docstrings.
   - `__init__.py` files: what they do and when to use them
3) Examples and docs
   - Add usage examples in an `examples/` folder showing:
     - Creating and using Task objects
     - Composition pattern with TaskManager
     - Proper package imports

### Problem solving (45–60 min)
- LeetCode: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

### Outcomes
- Well-structured code, easier imports, and clear object models.

### Deliverables
- Refactored package layout; examples runnable with instructions.
- Completed OOP exercises from `day01_exercises.md` (mandatory for promotion gate).
- Tests for Task, TaskManager, and other classes.

### Submission checklist
- [ ] Public APIs documented via module docstrings
- [ ] Imports are stable and simple
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


