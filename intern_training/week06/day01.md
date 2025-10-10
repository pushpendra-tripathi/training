## Week 6 · Day 1 — Authentication & Authorization

### Problem Definition (Answer BEFORE starting)
**What exactly are you building today?**  
A complete authentication system with login/logout/signup flows, plus per-user data isolation so users only see their own tasks.

**Why does this matter for Django?**  
Most Django applications require authentication and authorization. Understanding the auth system, decorators, and per-user filtering is essential for building secure applications.

**What does success look like?**  
- Login/logout/signup working correctly
- Users can only access their own tasks
- Unauthenticated users redirected to login

---

### Objectives
- Implement Django authentication system
- Add per-user data access
- Secure views with login requirements

### Tasks
1) Django Auth System
   - User model (built-in)
   - django.contrib.auth views
   - Login, logout, signup flows
   - Password reset (email simulation)

2) Authentication Views
   - LoginView: login page
   - LogoutView: logout redirect
   - SignupView: user registration
   - PasswordChangeView (optional)

3) Templates
   - login.html
   - signup.html  
   - Logged-in user display in navigation

4) Authorization
   - @login_required decorator
   - LoginRequiredMixin for CBVs
   - Add owner field to Task model (ForeignKey to User)
   - Automatically set owner on task creation
   - Filter QuerySets by request.user

5) Messages & Redirects
   - Success message on login/logout/signup
   - Redirect after login: LOGIN_REDIRECT_URL
   - Redirect unauthenticated users: LOGIN_URL

6) Problem solving (2-3 problems from ProblemBank_Django.md)
   - Core: Auth flows implementation
   - Stretch: Per-user filtering
   - Stretch: Custom user model or permissions

### Outcomes
- Full authentication system working
- Users only see their own tasks
- Unauthorized access properly blocked

### Deliverables
- Login/logout/signup views and templates
- Task model with owner field
- Migration for owner field
- All views restricted to authenticated users
- QuerySets filtered by request.user
- Messages for auth actions
- 2-3 auth problems solved

### Submission checklist
- [ ] Auth system functional
- [ ] Per-user data isolation working
- [ ] Unauthorized access blocked
- [ ] Messages displaying correctly
- [ ] 2+ auth problems solved
- [ ] Code passes quality tools
- [ ] **Daily reflection completed** (see [DAILY_TEMPLATE.md](../../DAILY_TEMPLATE.md)):
  - [ ] Problem definition answered before coding
  - [ ] Can explain why today's work matters for Django
  - [ ] Documented patterns learned and when to apply them




