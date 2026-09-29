from datetime import datetime
from typing import override

from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    class Meta:
        get_latest_by = "-created_at"
        ordering = ["-created_at"]

    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=100, default="Todo")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks", default=1
    )

    @override
    def __str__(self):
        return str(self.title)
