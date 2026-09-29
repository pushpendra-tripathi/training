from django.contrib import admin
from django.contrib.auth.models import User

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ["title", "status", "due_date", "created_at", "owner"]
    list_display = ["title", "status", "due_date", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["status", "due_date"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.register(Task, TaskAdmin)
