## Week 6 · Day 2 — Advanced Forms & Validation

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
Advanced form validation with cross-field rules, formsets for batch operations, and improved UX with better error feedback.

**Why does this matter for Django?**  
Complex forms require sophisticated validation. Understanding formsets and advanced validation patterns enables you to build robust, user-friendly forms for real-world Django applications.

**What does success look like?**  
- Cross-field validation working correctly
- Formsets allowing batch task creation
- Clear, helpful error messages for all validation failures

---

### Objectives
- Master advanced form validation patterns
- Implement formsets for multiple objects
- Add AJAX form submission (optional)

### Tasks
1) Advanced Form Validation
   - Field-level: clean_<fieldname>()
   - Form-level: clean() for cross-field validation
   - Custom validators as functions
   - ValidationError with error codes
   - Non-field errors

2) Form Widgets
   - Customize widget rendering
   - DateInput with HTML5 date picker
   - Textarea with custom attrs
   - Select with custom choices

3) Formsets
   - formset_factory for multiple forms
   - ModelFormSet for model instances
   - Inline formsets for related models
   - Validation across formset
   - Use case: batch task creation

4) Form UX Improvements
   - Sticky form data on errors
   - Field errors next to fields
   - Non-field errors at top
   - Success messages
   - Disabled submit during processing (optional JS)

5) AJAX Forms (Optional)
   - Submit form without page reload
   - Return JSON response
   - Display errors inline with JS
   - Update page content dynamically

6) Problem solving (2-3 problems)
   - Core: Complex validation rules
   - Stretch: Formsets implementation
   - Challenge: AJAX form submission

### Outcomes
- Robust forms with comprehensive validation
- Better UX with clear error feedback
- Formsets for batch operations

### Deliverables
- Enhanced TaskForm with:
  - Cross-field validation
  - Custom validators
  - Improved error display
- Formset for batch task creation
- AJAX form (optional)
- 2-3 advanced form problems solved

### Submission checklist
- [ ] Advanced validation working
- [ ] Formset functional
- [ ] Error display clear and helpful
- [ ] 2+ form problems solved
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them




