## Week 5 · Day 5 — Testing Django Applications

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A comprehensive Django test suite covering models, views, and forms, with >80% test coverage.

**Why does this matter for Django?**  
Testing is essential for Django applications. Understanding Django's test framework, the test client, and coverage tools ensures your code is reliable and maintainable.

**What does success look like?**  
- All models, views, and forms tested
- Test coverage >80%
- All tests passing with `python manage.py test`

---

### Objectives
- Write tests for Django models, views, and forms
- Use Django TestCase and test client
- Achieve >80% test coverage

### Tasks
1) Django Testing Basics
   - TestCase vs. pytest-django
   - Test database creation/destruction
   - Fixtures and setUpTestData
   - Test isolation

2) Model Tests
   - Test model creation
   - Test __str__ method
   - Test custom methods
   - Test model validation
   - Test model managers

3) View Tests
   - Django test client: self.client
   - GET requests: self.client.get()
   - POST requests: self.client.post()
   - Assertions: status_code, templates_used, context
   - Testing redirects
   - Testing authentication required

4) Form Tests
   - Test valid form data
   - Test invalid form data
   - Test custom validation
   - Test error messages

5) Coverage
   - Install coverage: `pip install coverage`
   - Run with coverage: `coverage run manage.py test`
   - Generate report: `coverage report`, `coverage html`
   - Aim for >80% coverage

6) Problem solving (2-3 problems from ProblemBank_Django.md)
   - Core: Model tests
   - Core: View tests
   - Core: Form tests
   - Stretch: Integration test for full CRUD flow

### Outcomes
- Comprehensive test suite
- Understanding of Django testing patterns
- Confidence in code correctness

### Deliverables
- Test suite covering:
  - Models (creation, methods, validation)
  - Views (all CRUD operations)
  - Forms (valid/invalid data, custom validation)
- Test coverage >80%
- Tests pass: `python manage.py test`
- Coverage report generated
- 2-3 testing problems solved

### Submission checklist
- [ ] Model tests passing
- [ ] View tests passing
- [ ] Form tests passing
- [ ] Coverage >80%
- [ ] 2+ testing problems solved
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


