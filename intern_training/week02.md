## Week 2 — OOP, Web Basics, Django Setup, CRUD, Admin, Templates

### Weekly learning goals
- Apply OOP in Python (dataclasses, composition, dunder methods) and structure packages.
- Understand web fundamentals: HTTP, REST, HTML semantics, CSS layout, basic JS.
- Create a Django project and implement a CRUD app with admin and templates.

### Daily schedule

#### Day 1 (Mon): OOP and packaging
- Topics
  - Classes, dataclasses, properties; composition vs inheritance; `__repr__` and equality.
  - Package organization and dependency boundaries.
- Hands-on
  - Refactor your Week 1 utilities into coherent packages with clear public APIs.
  - Add type-friendly docstrings and examples in module docstrings.
- Problem solving (45–60 min)
  - From LeetCode: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/), [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- Deliverables
  - Refactored modules with clear separation of concerns; format/lint clean.

#### Day 2 (Tue): Web basics
- Topics
  - HTTP verbs, status codes; static vs dynamic pages; progressive enhancement.
  - HTML semantics, CSS layout (Flexbox), minimal JS to fetch JSON and render.
- Hands-on
  - Build a static page that renders your energy insights from a JSON file; include basic styling.
- Problem solving
  - From Project Euler: [Problem 3](https://projecteuler.net/problem=3)
  - From LeetCode: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- Deliverables
  - Static site folder with `index.html`, `styles.css`, and a small `app.js`.

#### Day 3 (Wed): Django project start
- Topics
  - Django project and app creation, URL routing, views, templates, static files.
  - Settings basics; development vs production considerations at a high level.
- Hands-on
  - Create `tasktracker` project and `tasks` app.
  - Implement a homepage and a tasks list view using a template; include CSRF in forms.
- Problem solving
  - From LeetCode: [Ransom Note](https://leetcode.com/problems/ransom-note/), [Plus One](https://leetcode.com/problems/plus-one/)
- Deliverables
  - `runserver` works; pages render; committed with clear messages.

#### Day 4 (Thu): Models, admin, CRUD
- Topics
  - Models and migrations; Django admin customization; forms/ModelForm; class-based views (ListView, CreateView, UpdateView, DeleteView).
- Hands-on
  - Create `Task` model (title, description, status, due_date, owner optional for now).
  - Register in admin with list display, filters, search.
  - Implement CRUD with CBVs and pagination on the list.
- Problem solving
  - From LeetCode: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
  - From Euler: [Problem 4](https://projecteuler.net/problem=4)
- Deliverables
  - CRUD flow works end-to-end; screenshots in README.

#### Day 5 (Fri): Templates and UX polish
- Topics
  - Template inheritance, static files, messages framework, basic form validation.
- Hands-on
  - Add base template, navigation, success/error messages, and simple search/filter on tasks.
- Problem solving
  - From LeetCode: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
  - From LeetCode: [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- Deliverables
  - Polished UI with template inheritance and messaging; format/lint clean.

### Weekend assignment
Polish and extend the Task Tracker:
- Add a `status` workflow (e.g., Todo, In-Progress, Done) with validation.
- Implement simple search by title and due-date filter; paginate results.
- Write a short user guide in `README.md` with screenshots.
- Ensure `black`, `isort`, `pylint` all pass locally; include a `Makefile` with `format`, `lint`, `run` targets.


