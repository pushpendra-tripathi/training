#### Usecases of taskmanager class with required modules

```python

from ctypes import resize

from Classes.data_class import Task, UrgentTask
from Classes.TaskManager import TaskManager
```

# 1. Create manager instance from TaskManager

```python
manager = TaskManager()
```

# 2. Add tasks using manager.add_task method

```python
manager.add_task(Task(title="Buy milk", description="Get 2 litresk", status="done"))
```

# to check if the task is added successfully use len function on manager

```python
print(len(manager)) # 1
```

# 3. To add urgent tasks use UrgentTask class

# Note: keep the date in same format

```python
manager.add_task(
UrgentTask(
title="Submit report",
description="Q4 report",
due_date="2026-10-04",
deadline="2026-11-01",
status="todo",
)
)

print(len(manager)) # should return "2" now
```

# 4. Use get_incomplete method to get all the incomplete tasks

```python
print(
manager.get_incomplete_tasks()
) # should return [UrgentTask(title='Submit report', description='Q4 report', status='todo', due_date='2026-10-04', deadline='2026-11-01')]
print(len(manager.get_incomplete_tasks())) # 1
```

# 5. Use get_completed_tasks method to get all completed tasks

```python
print(
manager.get_completed_tasks()
) # should return [Task(title='Buy milk', description='Get 2 litresk', status='done', due_date=None)]

print(len(manager.get_completed_tasks())) # 1
```

# 6. Use mark_task_complete method to mark a task complete

```python
result = manager.mark_task_complete(title="Submit report")
print(result) # return True if the the task with that specific title is found

print(len(manager.get_completed_tasks())) # 3
```
