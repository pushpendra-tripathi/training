## Week 5 · Day 4 — Forms, Validation & Admin

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
ModelForms with custom validation, a fully customized Django admin, and the messages framework for user feedback.

**Why does this matter for Django?**  
Forms and validation are critical for data integrity. The Django admin is a powerful productivity tool. Understanding both enables you to build robust, user-friendly Django applications.

**What does success look like?**  
- Forms with field-level and form-level validation working
- Admin with list_display, list_filter, search, and custom actions
- Messages providing feedback on all user actions

---

### Objectives
- Master ModelForms and validation
- Customize Django admin for productivity
- Implement messages framework

### Tasks
1) ModelForm Basics
   - Create TaskForm(ModelForm)
   - Meta class: model, fields, widgets
   - Form rendering in templates
   - CSRF protection

2) Form Validation
   - Field-level validation with clean_<fieldname>()
   - Form-level validation with clean()
   - Custom validators
   - ValidationError with error messages
   - Example: ensure due_date is in future

3) Messages Framework
   - messages.success(), messages.error(), messages.info()
   - Display messages in base template
   - Message tags and styling

4) Django Admin
   - Register models: admin.site.register()
   - ModelAdmin customization:
     - list_display: columns to show
     - list_filter: filters in sidebar
     - search_fields: search functionality
     - ordering: default sort order
     - date_hierarchy: date drill-down
   - Admin actions: custom bulk actions
   - Inline editing

5) Problem solving (3-4 problems from ProblemBank_Django.md)
   - Core: ModelForm with custom validation
   - Stretch: Form with multiple models
   - Core: Custom admin configuration
   - Stretch: Inline admin

### Outcomes
- Forms with robust validation
- Admin customized and productive
- Messages providing user feedback

### Deliverables
- TaskForm with custom validation
- Create/Update views using ModelForm
- Messages framework integrated
- Admin configured with:
  - list_display, list_filter, search_fields
  - At least 1 custom admin action
- 3-4 form/admin problems solved

### Submission checklist
- [ ] Forms with validation working
- [ ] Messages displaying correctly
- [ ] Admin customized and useful
- [ ] Custom admin action implemented
- [ ] 3+ form/admin problems solved
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them


