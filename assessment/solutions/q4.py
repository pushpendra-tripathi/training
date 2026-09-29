
'''from django.contrib import admin
from .models import Task

class TaskAdmin:
    list_display = ("title", "status", "due_date")
    search_fields = "title"
    list_filter = "status"

admin.site.register(Task)'''

# The fileds should be in an iterable list

from django.contrib import admin
from .models import Task


class TaskAdmin:
    list_display = ['title','status','due_date']
    search_fields = ['title']
    list_filter = ['status']

admin.site.register(Task)


