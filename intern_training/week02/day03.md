## Week 2 · Day 3 — Django Project Setup

### Objectives
- Create a Django project and first app; wire URLs, views, and templates.

### Tasks
1) Project bootstrap
   - Create a new Django project called `tasktracker` with a `tasks` app
   - Configure settings to:
     - Register the `tasks` app
     - Set up a project-level `templates/` directory
     - Configure static files (CSS, images, etc.)
   - Organize your directory structure logically:
     - Project-level templates for base layout
     - App-level templates for task-specific pages
     - Static files directory for CSS

2) First views and URL routing
   - Create a home page view that welcomes users to the Task Tracker
   - Create a tasks list view that displays sample task data (hardcoded for now)
   - Set up URL routing:
     - App-level URLs for the tasks app with named patterns
     - Include app URLs in the project's main URL config
     - Use Django's `app_name` for URL namespacing
   - Create templates:
     - A base template with navigation and common layout
     - Home page template extending the base
     - Task list template extending the base and displaying sample tasks
   - Ensure navigation links use Django's `{% url %}` template tag

3) Static files setup
   - Create a basic stylesheet with:
     - Reset/normalize styles
     - Navigation bar styling
     - Basic layout and typography
   - Configure Django to serve static files in development
   - Load static files in your base template using `{% load static %}`
   - Verify static files are loading correctly (check browser DevTools)

### Expected Result
- You can navigate to the home page and see a welcome message
- The tasks list page shows sample hardcoded tasks
- Navigation links between pages work correctly
- CSS styling is applied and visible
- All URLs use Django's URL namespacing and named patterns

### Problem solving (45–60 min)
- LeetCode: [Ransom Note](https://leetcode.com/problems/ransom-note/), [Plus One](https://leetcode.com/problems/plus-one/)

### Outcomes
- Local server running with working pages and navigation.

### Deliverables
- Project committed with instructions to run (`venv`, `migrate`, `runserver`).

### Submission checklist
- [ ] Home and list pages render
- [ ] Base template in place
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`


