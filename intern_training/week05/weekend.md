## Week 5 · Weekend Assignment — Fullstack Mini Demo

### Objective
Ship a small fullstack feature: task details page with comments.

### Problem Statement
Extend the Task Tracker with a commenting feature that demonstrates fullstack integration:
- **Backend**: REST API endpoint for task comments
- **Frontend**: JavaScript UI to display and add comments
- **Integration**: Frontend consumes backend API with proper auth and error handling

This demonstrates your ability to build and integrate both sides of a modern web application.

### Architecture Overview
```
Backend (Django + DRF)              Frontend (HTML/CSS/JS)
┌─────────────────────┐            ┌──────────────────────┐
│ /api/tasks/         │◄───────────┤ fetch('/api/tasks/') │
│ /api/tasks/<id>/    │            │ Task list & detail   │
│ /api/tasks/<id>/    │            │                      │
│   comments/         │◄───────────┤ Comments component   │
│   - GET (list)      │            │ - Display list       │
│   - POST (create)   │            │ - Add new comment    │
└─────────────────────┘            └──────────────────────┘
```

### Expected Features

#### Backend: Comments API

**Model**:
```python
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments')
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
```

**Endpoint**: `GET /api/tasks/<task_id>/comments/`
```json
[
  {
    "id": 1,
    "text": "This is urgent, let's prioritize it",
    "author": "john",
    "created_at": "2025-10-15T14:30:00Z"
  },
  {
    "id": 2,
    "text": "Updated the timeline in the description",
    "author": "sarah",
    "created_at": "2025-10-15T15:45:00Z"
  }
]
```

**Endpoint**: `POST /api/tasks/<task_id>/comments/`
```bash
curl -X POST http://localhost:8000/api/tasks/1/comments/ \
  -H "Authorization: Token abc123..." \
  -H "Content-Type: application/json" \
  -d '{"text": "Great progress on this!"}'
```

**Success** (201):
```json
{
  "id": 3,
  "text": "Great progress on this!",
  "author": "current_user",
  "created_at": "2025-10-15T16:00:00Z"
}
```

**Validation Error** (400):
```json
{
  "text": ["This field is required."]
}
```

**Permissions**:
- Must be authenticated to view/create comments
- Can only comment on tasks you own or have access to
- Return 401 if not authenticated, 403 if no permission

#### Frontend: Comments UI

**Task Detail Page** (`task-detail.html`):
```
┌─────────────────────────────────────┐
│ Task: Complete Project Documentation│
│ Status: In Progress                 │
│ Due: 2025-11-15                     │
├─────────────────────────────────────┤
│ Comments (3)                        │
├─────────────────────────────────────┤
│ john • 2 hours ago                  │
│ This is urgent, let's prioritize it │
├─────────────────────────────────────┤
│ sarah • 1 hour ago                  │
│ Updated the timeline                │
├─────────────────────────────────────┤
│ [Add a comment...]                  │
│ [Post Comment]                      │
└─────────────────────────────────────┘
```

**States to Handle**:
1. **Loading**: "Loading comments..." spinner
2. **Empty**: "No comments yet. Be the first to comment!"
3. **Error**: "Failed to load comments. [Retry]"
4. **Success**: Display comments with formatting

**Add Comment Flow**:
1. User types in textarea
2. Click "Post Comment"
3. Show loading state on button ("Posting...")
4. On success: Clear textarea, prepend new comment to list, show success message
5. On error: Show error message below form, keep text in textarea

**JavaScript Structure**:
```javascript
// api.js - API client
async function getComments(taskId) { ... }
async function createComment(taskId, text) { ... }

// comments.js - Comments component
function renderComments(comments) { ... }
function attachCommentFormHandler() { ... }

// app.js - Main initialization
document.addEventListener('DOMContentLoaded', () => {
  loadTaskDetail();
  loadComments();
});
```

### Example User Journey
```
1. Navigate to task detail page (/tasks/1/)
2. Scroll to comments section
3. See existing comments with authors and timestamps
4. Type "Great work!" in comment textarea
5. Click "Post Comment"
6. Button shows "Posting..." (disabled)
7. New comment appears at top of list
8. Success message: "Comment added successfully"
9. Textarea is cleared and ready for next comment
10. If offline/error: See "Failed to post comment. Please try again."
```

### Error Scenarios to Test
- **Network failure**: Show retry option
- **Auth expired**: Redirect to login
- **Empty comment**: Show validation "Comment cannot be empty"
- **Server error (500)**: Show friendly message
- **Task not found (404)**: Show "Task not found"

### Step-by-step tasks
1) Backend: comments endpoint
   - Add `/api/tasks/<id>/comments/` (list and create) scoped to owner.
   - Serializer validation for non-empty text.
2) Frontend: comments UI
   - Render existing comments on task details; add form to post a new comment.
3) States and errors
   - Include loading, error, and empty states; show validation errors from API.
4) Docs
   - Document how to run both backend and frontend; include example commands.
5) Quality
   - Run `black .`, `isort .`, `pylint **/*.py` locally on backend; fix issues.

### Acceptance criteria
- New endpoint implemented, documented, and accessible.
- Frontend page shows comments and allows adding a comment successfully.
- Clear error handling; README updated; screenshots/GIF included.

