'''
def task_report():
    lines = []
    for task in Task.objects.all():
        lines.append(f"{task.title} — owner: {task.owner.email}")
    return lines
'''

# The function above is running the querry for each task and then another querry on owner field
# thereby running the n+1 querries
# We can fix this by using the select_related method 

from .models import Task

def task_report():
    tasks = Task.objects.select_related('owner').all()
    lines  = []
    for task in tasks:
        lines.append(f'{task.title}-owner-owner:{task.owner.email}')

    return lines

