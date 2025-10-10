## Week 5 · Day 3 — Templates & Django Template Language

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A complete template system with inheritance, reusable partials, custom template tags/filters, and static file configuration.

**Why does this matter for Django?**  
Templates are how Django renders HTML. Understanding template inheritance, the DTL, and custom tags/filters enables you to build maintainable, DRY frontend code.

**What does success look like?**  
- All views use template inheritance (no duplicate HTML)
- At least 2 reusable partials extracted
- Custom filter working correctly

---

### Objectives
- Master template inheritance and the Django Template Language (DTL)
- Build reusable template components
- Create custom template tags and filters

### Tasks
1) Template Inheritance
   - Create `base.html` with blocks: title, content, extra_css, extra_js
   - Extend base in list/detail/form templates
   - Block override and {{ block.super }}

2) Django Template Language
   - Variables: {{ variable }}
   - Tags: {% if %}, {% for %}, {% url %}, {% static %}, {% csrf_token %}
   - Filters: {{ value|filter }}, {{ value|filter:arg }}
   - Template comments: {# comment #}

3) Template Includes
   - Partials for reusable components
   - {% include "partial.html" %}
   - Pass context to includes

4) Built-in Filters
   - date, time, truncatechars, linebreaks
   - default, length, join
   - safe, escape

5) Custom Template Tags/Filters
   - Create `templatetags/` directory
   - Simple filter: status_badge (returns CSS class)
   - Simple tag: get_recent_tasks

6) Static Files
   - Configure STATIC_URL, STATIC_ROOT
   - {% load static %}
   - {% static 'css/style.css' %}

7) Problem solving (2-3 problems from ProblemBank_Django.md)
   - Core: Template inheritance system
   - Stretch: Custom template tags
   - Stretch: Template with context processors

### Outcomes
- DRY templates with inheritance
- Reusable partials
- Custom filters/tags working

### Deliverables
- base.html with blocks
- All views use template inheritance
- At least 2 partials extracted
- 1 custom filter implemented
- Static files configured
- 2-3 template problems solved

### Submission checklist
- [ ] Template inheritance working
- [ ] Partials used for reusable components
- [ ] Custom filter created
- [ ] Static files loading
- [ ] 2+ template problems solved
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


