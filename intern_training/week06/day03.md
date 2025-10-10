## Week 6 · Day 3 — Pagination, Search & Filtering

### Objectives
- Implement server-side pagination
- Add search functionality
- Build filtering with query parameters

### Tasks
1) Pagination
   - Django Paginator class
   - Page object methods
   - ListView with pagination
   - Pagination controls in template
   - Preserve query params in pagination links

2) Search
   - Search form in template
   - Filter QuerySet with Q objects
   - Search across multiple fields
   - Case-insensitive search: __icontains
   - Preserve search query in pagination

3) Filtering
   - Filter by status, priority, date range
   - Filter links in template
   - Active filter highlighting
   - Combine filters with search
   - Clear filters option

4) Q Objects
   - Complex queries with OR/AND
   - Q(field=value) | Q(other=value)
   - ~Q() for NOT
   - Combining Q objects

5) URL Query Parameters
   - ?page=2&q=search&status=done
   - request.GET dictionary
   - Preserve params across actions
   - Clean URL handling

6) Problem solving (2 problems)
   - Core: Pagination + search + filtering
   - Stretch: Complex queries with Q objects

### Outcomes
- Usable list interface
- Search and filters working together
- Clean URL parameter handling

### Deliverables
- Task list view with:
  - Pagination (10 per page)
  - Search by title/description
  - Filters: status, priority, date range
  - Active filter indication
  - Preserved state in URLs
- 2 pagination/search problems solved

### Submission checklist
- [ ] Pagination working correctly
- [ ] Search functional
- [ ] Filters working
- [ ] URL params preserved
- [ ] 2+ problems solved
- [ ] Code passes quality tools




