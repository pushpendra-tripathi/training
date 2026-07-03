## Problem Bank — Object-Oriented Programming (18 problems)

**Target**: Week 2. Pick 4-6 problems daily; focus on design patterns and testing.

### Core (must) — Classes & Encapsulation

1) **Bank Account class**
   - Methods: deposit, withdraw, get_balance
   - Rules: balance cannot go negative
   - Tests: overdraft attempt, valid transactions
   ```python
   acc = BankAccount(initial_balance=100)
   acc.deposit(50)  # balance: 150
   acc.withdraw(30)  # balance: 120
   acc.withdraw(200)  # raises InsufficientFundsError
   ```

2) **Rectangle class with properties**
   - Attributes: width, height (validated >0)
   - Properties: area, perimeter (computed)
   - Methods: `__repr__`, `__eq__`
   ```python
   r = Rectangle(width=5, height=3)
   print(r.area)  # 15
   print(r.perimeter)  # 16
   ```

3) **Student class with grade tracking**
   - Attributes: name, grades (private list)
   - Methods: add_grade, average, is_passing (≥60)
   - Edge: empty grades list
   ```python
   s = Student("Alice")
   s.add_grade(85)
   s.add_grade(92)
   print(s.average())  # 88.5
   print(s.is_passing())  # True
   ```

4) **Shopping Cart**
   - Methods: add_item, remove_item, total_cost, apply_discount
   - Items: (name, price, quantity)
   - Tests: empty cart, discount edge cases
   ```python
   cart = ShoppingCart()
   cart.add_item("Apple", price=1.50, quantity=3)
   cart.add_item("Banana", price=0.75, quantity=2)
   print(cart.total_cost())  # 6.00
   cart.apply_discount(0.10)  # 10% off
   print(cart.total_cost())  # 5.40
   ```

5) **Temperature converter class**
   - Methods: to_fahrenheit, to_celsius, to_kelvin
   - Validation: Kelvin cannot be negative
   - Use: classmethod for different constructors
   ```python
   t = Temperature.from_celsius(25)
   print(t.to_fahrenheit())  # 77.0
   print(t.to_kelvin())  # 298.15
   ```

### Core (must) — Inheritance & Polymorphism

6) **Shape hierarchy**
   - Base: Shape (abstract area, perimeter methods)
   - Subclasses: Circle, Rectangle, Triangle
   - Tests: polymorphic list of shapes
   ```python
   shapes = [Circle(radius=5), Rectangle(4,6), Triangle(3,4,5)]
   for s in shapes:
       print(f"{s.__class__.__name__}: area={s.area()}")
   ```

7) **Employee hierarchy**
   - Base: Employee (name, base_salary, calculate_pay abstract)
   - Subclasses: HourlyEmployee, SalariedEmployee, ContractEmployee
   - Override: calculate_pay with different logic
   ```python
   emp1 = HourlyEmployee("Alice", hourly_rate=25, hours_worked=40)
   emp2 = SalariedEmployee("Bob", annual_salary=60000)
   print(emp1.calculate_pay())  # 1000
   print(emp2.calculate_pay())  # 5000 (monthly)
   ```

8) **Vehicle hierarchy with method overriding**
   - Base: Vehicle (make, model, start, stop)
   - Subclasses: Car, Motorcycle, ElectricCar
   - Override: start() with different messages
   - Tests: super() usage

### Stretch (nice) — Composition over Inheritance

9) **Library system**
   - Classes: Book, Member, Library
   - Composition: Library contains list of Books and Members
   - Methods: check_out, return_book, find_available_books
   ```python
   lib = Library()
   lib.add_book(Book("1984", "Orwell"))
   lib.add_member(Member("Alice", member_id=1))
   lib.check_out(book_title="1984", member_id=1)
   ```

10) **Task Manager with composition**
    - Classes: Task, TaskList, TaskManager
    - TaskManager has multiple TaskLists (e.g., "work", "personal")
    - Methods: add_task, complete_task, list_by_status, list_by_tag
    ```python
    tm = TaskManager()
    tm.add_task("work", Task(title="Review PR", priority="high"))
    tm.add_task("personal", Task(title="Grocery", priority="low"))
    print(tm.list_by_priority("high"))
    ```

11) **Game character with inventory**
    - Classes: Character, Item, Inventory
    - Character has-a Inventory (composition)
    - Methods: add_to_inventory, use_item, total_weight
    - Tests: weight limits, item uniqueness

### Stretch (nice) — Design Patterns

12) **Singleton pattern: Configuration manager**
    - Ensure only one instance exists
    - Methods: get, set, save_to_file, load_from_file
    ```python
    cfg1 = Config.get_instance()
    cfg2 = Config.get_instance()
    assert cfg1 is cfg2  # same object
    ```

13) **Factory pattern: Notification system**
    - Classes: EmailNotification, SMSNotification, PushNotification
    - Factory: create_notification(type, message)
    - Polymorphic: send() method
    ```python
    notif = NotificationFactory.create("email", "Hello!")
    notif.send()
    ```

14) **Observer pattern: Event system**
    - Classes: Subject, Observer
    - Subject notifies all observers on state change
    - Use case: stock price updates to multiple dashboards

### Challenge (bonus)

15) **Dataclass with validation**
    - Use @dataclass decorator
    - Add __post_init__ validation
    - Frozen dataclass for immutability
    ```python
    @dataclass
    class Person:
        name: str
        age: int
        
        def __post_init__(self):
            if self.age < 0:
                raise ValueError("Age cannot be negative")
    ```

16) **Custom container class**
    - Implement __len__, __getitem__, __setitem__, __iter__
    - Behaves like a list but with custom behavior
    - Tests: slicing, iteration, index errors

17) **Multiple inheritance: Mixins**
    - Classes: TimestampMixin, ValidationMixin, LoggingMixin
    - Combine with main class using multiple inheritance
    - Resolve: method resolution order (MRO)

18) **Context manager class**
    - Implement __enter__ and __exit__
    - Use case: Database connection manager
    - Handle: exceptions in managed code
    ```python
    with DatabaseConnection("mydb.db") as db:
        db.execute("SELECT * FROM users")
    # connection auto-closed even if exception occurs
    ```

### Guidance
- Use type hints for all class attributes and methods
- Implement `__repr__` and `__str__` for debugging
- Write tests for:
  - Happy path
  - Edge cases (empty, negative, None)
  - Exception handling
- Document: class purpose, design decisions, complexity
- Prefer composition over inheritance where appropriate
- Apply SOLID principles where relevant


