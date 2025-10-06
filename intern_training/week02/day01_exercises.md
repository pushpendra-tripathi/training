# Week 2 Day 1 — OOP Fundamentals Practice Exercises

## Part 1: Basic Classes

### Exercise 1: Person Class
```python
class Person:
    """Represent a person with name and age."""
    
    def __init__(self, name: str, age: int):
        pass
    
    def introduce(self) -> str:
        """Return introduction string."""
        pass
    
    def is_adult(self) -> bool:
        """Return True if age >= 18."""
        pass
```

Test it:
```python
person = Person("Alice", 25)
print(person.introduce())  # "Hi, I'm Alice and I'm 25 years old."
print(person.is_adult())   # True
```

### Exercise 2: BankAccount with Encapsulation
```python
class BankAccount:
    """Bank account with balance management."""
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance  # "private" attribute
    
    @property
    def balance(self) -> float:
        """Get current balance (read-only from outside)."""
        pass
    
    def deposit(self, amount: float) -> None:
        """Deposit money (must be positive)."""
        pass
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money. Return True if successful, False if insufficient funds."""
        pass
    
    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        pass
```

## Part 2: Inheritance

### Exercise 3: Task Hierarchy
```python
class Task:
    """Base task class."""
    
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.completed = False
    
    def mark_complete(self) -> None:
        """Mark task as completed."""
        pass
    
    def __repr__(self) -> str:
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"

class UrgentTask(Task):
    """Urgent task with deadline."""
    
    def __init__(self, title: str, description: str, deadline: str):
        super().__init__(title, description)
        self.deadline = deadline
    
    def is_overdue(self, current_date: str) -> bool:
        """Check if task is overdue."""
        pass
    
    def __repr__(self) -> str:
        """Override to show deadline."""
        base = super().__repr__()
        return f"{base} (Due: {self.deadline})"
```

## Part 3: Composition

### Exercise 4: TaskManager
```python
class TaskManager:
    """Manage a collection of tasks."""
    
    def __init__(self):
        self.tasks: list[Task] = []
    
    def add_task(self, task: Task) -> None:
        """Add a task to the list."""
        pass
    
    def get_incomplete_tasks(self) -> list[Task]:
        """Return all incomplete tasks."""
        pass
    
    def get_completed_tasks(self) -> list[Task]:
        """Return all completed tasks."""
        pass
    
    def mark_task_complete(self, title: str) -> bool:
        """Find task by title and mark complete. Return True if found."""
        pass
    
    def __len__(self) -> int:
        """Return number of tasks."""
        pass
```

Usage:
```python
manager = TaskManager()
manager.add_task(Task("Buy milk", "Get 2 liters"))
manager.add_task(UrgentTask("Submit report", "Q4 report", "2024-12-31"))

print(len(manager))  # 2
print(manager.get_incomplete_tasks())
```

## Part 4: Dataclasses

### Exercise 5: Convert Task to Dataclass
```python
from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class Task:
    """Task with validation."""
    title: str
    description: str
    status: Literal["todo", "in_progress", "done"] = "todo"
    due_date: date | None = None
    
    def __post_init__(self):
        """Validate after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        
        if self.due_date and self.due_date < date.today():
            raise ValueError("Due date cannot be in the past")
    
    def transition_to(self, new_status: Literal["todo", "in_progress", "done"]) -> None:
        """Change status with validation."""
        valid_transitions = {
            "todo": ["in_progress"],
            "in_progress": ["done", "todo"],
            "done": ["todo"]
        }
        
        if new_status not in valid_transitions[self.status]:
            raise ValueError(f"Cannot transition from {self.status} to {new_status}")
        
        self.status = new_status
```

Test:
```python
task = Task("Write tests", "Unit tests for utils")
task.transition_to("in_progress")
print(task.status)  # "in_progress"

try:
    task.transition_to("todo")  # Valid: can go back
except ValueError as e:
    print(e)
```

## Part 5: Practical OOP

### Exercise 6: Shopping Cart
```python
@dataclass
class Product:
    name: str
    price: float
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

class ShoppingCart:
    """Shopping cart with products."""
    
    def __init__(self):
        self._items: dict[str, tuple[Product, int]] = {}  # name -> (product, quantity)
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add product to cart."""
        pass
    
    def remove_item(self, product_name: str) -> None:
        """Remove product from cart."""
        pass
    
    def get_total(self) -> float:
        """Calculate total price."""
        pass
    
    def __len__(self) -> int:
        """Return total number of items (considering quantities)."""
        pass
```

## Testing Your OOP Code

Create `tests/test_oop.py`:
```python
import unittest
from datetime import date

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test", "Description")
        self.assertEqual(task.status, "todo")
    
    def test_empty_title_raises_error(self):
        with self.assertRaises(ValueError):
            Task("", "Description")
    
    def test_status_transition(self):
        task = Task("Test", "Desc")
        task.transition_to("in_progress")
        self.assertEqual(task.status, "in_progress")
    
    def test_invalid_transition_raises_error(self):
        task = Task("Test", "Desc")
        with self.assertRaises(ValueError):
            task.transition_to("done")  # Can't go from todo to done directly

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task1 = Task("Task 1", "First task")
        self.task2 = Task("Task 2", "Second task")
    
    def test_add_task(self):
        self.manager.add_task(self.task1)
        self.assertEqual(len(self.manager), 1)
    
    # Add more tests...

if __name__ == "__main__":
    unittest.main()
```

## Success Criteria

- [ ] Can explain the difference between instance and class attributes
- [ ] Can implement `__init__`, `__repr__`, `__str__`, `__eq__`
- [ ] Understands when to use `@property` decorator
- [ ] Can explain inheritance vs composition (and when to use each)
- [ ] Can use `super()` correctly
- [ ] Understands dataclasses and `__post_init__`
- [ ] All code passes type checking and linting
- [ ] Can write unit tests for classes

## Bonus: Advanced OOP

1. **Abstract Base Classes**: Create an abstract `Storage` interface with `save()` and `load()` methods
2. **Class Methods**: Add `Task.from_dict(data: dict) -> Task` factory method
3. **Static Methods**: Add `Task.is_valid_status(status: str) -> bool`
4. **Multiple Inheritance**: Explore (but prefer composition in real code!)
