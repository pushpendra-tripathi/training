## Week 4 — Templates Consolidation: UI, Admin, and Tests

### Weekly learning goals
- Build upon Week 2 templates and Week 3 auth/APIs to deliver a polished, template-first app.
- Prepare the codebase so it’s straightforward to add a frontend client in Week 5 (bonus).
- Keep backend code clean with local `black`, `isort`, and `pylint`.

### Daily schedule

#### Day 1 (Mon): Templates Deep Dive
- Topics
  - Inheritance, blocks, includes, built-in and custom filters/tags.
- Hands-on
  - Create `base.html`, extract partials, and add a custom filter for task status.
- Problem solving (45–60 min)
  - From LeetCode: Valid Parentheses (revisit with stack variations)
- Deliverables
  - DRY templates with base and partials; notes on custom filter.

#### Day 2 (Tue): Forms, Messages, and Validation
- Topics
  - ModelForm polish, messages framework, error display.
- Hands-on
  - Style fields, show field/non-field errors, and surface success/error messages.
- Problem solving
  - From LeetCode: Detect Capital; Reverse Linked List
- Deliverables
  - Friendly forms and clear feedback on actions.

#### Day 3 (Wed): List Pagination, Search, and Sorting
- Topics
  - Server-side pagination, query-based search and sorting.
- Hands-on
  - Add pagination controls; implement `?q=` search and `?sort=` (due_date/status).
- Problem solving
  - From LeetCode: Valid Sudoku
- Deliverables
  - Usable list page with pagination, search, and sorting.

#### Day 4 (Thu): Admin Polish and Template Customization
- Topics
  - Admin list/filters/search, custom actions, simple branding.
- Hands-on
  - Configure columns/filters; add a custom action; minor template tweaks.
- Problem solving
  - From LeetCode: Group Anagrams
- Deliverables
  - Productive admin with a working custom action.

#### Day 5 (Fri): Testing Basics and Template Refinements
- Topics
  - Tests for views/forms; verifying blocks/includes/custom filters.
- Hands-on
  - Add tests for list/search/pagination and form validation; tidy templates.
- Problem solving
  - From LeetCode: Move Zeroes
- Deliverables
  - Tests passing and polished UI; updated README.

### Weekend assignment — Templates and Admin Consolidation
- Ensure base/partials/custom filters in use across pages.
- Verify list (pagination/search/sorting) and detail page polish.
- Confirm admin filters/search and custom action work; capture a screenshot.
- Update README with setup/testing and screenshots; run `black`, `isort`, `pylint` locally.

### Promotion gate (advance to Week 5 if all met)
- Required to advance:
  - Templates are DRY (base + includes); custom filter works.
  - List supports pagination/search/sorting; forms show clear validation.
  - Admin is functional with custom action; tests pass locally.


