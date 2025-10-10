# Daily Work Template

> Copy this template to your daily log each day. Fill it out BEFORE coding and AFTER finishing.

## Date: YYYY-MM-DD | Week X, Day Y

---

## Part 1: UNDERSTAND THE PROBLEM (Complete BEFORE coding)

### 1. What exactly am I building/learning today?
**In one clear sentence**:

*Example: "Today I'm building a CSV validation module that catches ALL errors before processing data."*

### 2. Why does this matter for production Django development?
**Connect today's work to real Django applications**:

*Example: "Django apps process user data. Invalid data crashes apps or corrupts databases. Proper validation prevents both."*

### 3. What does success look like by end of day?
**Specific, testable outcomes** (not vague "understanding"):
- [ ] Specific deliverable 1
- [ ] Specific deliverable 2
- [ ] Specific deliverable 3
- [ ] Tests passing with >85% coverage
- [ ] Code passes quality tools

*Example:*
- *[ ] CSV validator that finds missing columns, type errors, and range violations*
- *[ ] Returns ALL errors (not just first), with row numbers*
- *[ ] Tests cover happy path + 5 error scenarios*
- *[ ] Documented with examples*

### 4. What are my constraints?
**What limits my approach?**:
- Knowledge: What do I NOT know yet? ______
- Resources: What help/docs do I need? ______
- Dependencies: What must be done first? ______

---

## Part 2: DEVISE A PLAN (Complete BEFORE coding)

### 5. What are the steps to achieve today's objective?
**Break into manageable chunks**:

1. [ ] Step 1: ______
2. [ ] Step 2: ______
3. [ ] Step 3: ______
4. [ ] Step 4: ______
5. [ ] Step 5: ______

### 6. What problems might I encounter?
**Anticipate obstacles**:
- Potential blocker 1: ______
  - Mitigation: ______
- Potential blocker 2: ______
  - Mitigation: ______

### 7. How will I verify success?
**Acceptance criteria BEFORE building**:
- [ ] Criterion 1: ______
- [ ] Criterion 2: ______
- [ ] Criterion 3: ______

---

## Part 3: CARRY OUT THE PLAN (During coding)

### 8. Execution Log
**Track progress and blockers**:

| Activity | Status | Notes |
|----------|--------|-------|
| Setup validator module | ✅ Done | Created basic structure |
| Implement column validation | ⏳ In Progress | Need to handle missing columns |
| Stuck: How to collect all errors? | ❌ Blocked | Asked mentor, solution: accumulate in list |
| Implement error collection | ✅ Done | Works! |

### 9. Code Decisions Made
**Document WHY, not just WHAT**:
- **Decision**: Used list to accumulate errors instead of raising immediately
  - **Why**: Need to show ALL errors to user, not just first
  - **Alternative considered**: Exceptions (rejected: stops on first error)
  
- **Decision**: ______
  - **Why**: ______
  - **Alternative considered**: ______

---

## Part 4: LOOK BACK (Complete AFTER finishing)

### 10. Did I achieve today's objective?
- [ ] Yes, completely
- [ ] Partially (explain below)
- [ ] No (explain below)

**Explanation if not 100%**:

### 11. What worked well today?
**Positive patterns to repeat**:
1. ______
2. ______
3. ______

### 12. What was difficult?
**Challenges encountered**:
1. ______
   - How I solved it: ______
   - What I learned: ______

2. ______
   - How I solved it: ______
   - What I learned: ______

### 13. What patterns/principles did I learn?
**Transferable knowledge**:
- Pattern 1: ______
  - When to use: ______
  - Example: ______
  
- Pattern 2: ______
  - When to use: ______
  - Example: ______

### 14. How does today's work connect to production Django?
**Make the link explicit**:

*Example: "Today's validation module is like Django's ModelForm validation. Both need to collect all errors, display them clearly, and prevent bad data from reaching the database."*

### 15. Quality Check
**Honest self-assessment**:
- [ ] Can I explain my code to a team member without looking at it?
- [ ] Would I deploy this to production? (If no, why not?)
- [ ] Are my tests comprehensive? (Edge cases covered?)
- [ ] Is my code readable? (Clear names, no magic numbers?)
- [ ] Did I document WHY, not just WHAT?

### 16. What would I do differently tomorrow?
**Continuous improvement**:
1. ______
2. ______

---

## Submission Checklist
- [ ] All code committed with clear messages
- [ ] Tests passing locally
- [ ] Code passes `black .`, `isort .`, `pylint **/*.py`
- [ ] README/docs updated
- [ ] This daily log completed and committed
- [ ] Tomorrow's problem defined (what am I building next?)

---

## Tomorrow's Setup (5-min preview)
**What's the problem for tomorrow?**:

**Why does it matter?**:

**Initial thoughts on approach**:

---

*Remember: Definition before motion. If you can't fill out Part 1 clearly, stop and ask for clarification.*

