"""
Form module
"""

import datetime
from typing import override

from dateutil.relativedelta import relativedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Task


class TaskForm(forms.ModelForm):
    """
    Task form
    """

    class Meta:
        """
        meta class for Task
        """

        model = Task
        fields = ["title", "description", "status", "due_date"]

    def clean_due_date(self):
        """
        due_date validation
        """
        deadline = self.cleaned_data.get("due_date")
        today = datetime.date.today()
        max_date = today + relativedelta(months=1)
        if deadline is not None:
            if deadline < today:
                raise ValidationError("due_date can't be in the past")
            elif deadline > max_date:
                print("max_date: ", max_date)
                print("today: ", today)
                raise ValidationError("due_date can't be greater than 4 weeks from now")
            return deadline

    def clean_status(self):
        """
        status validation
        """
        status = self.cleaned_data.get("status")

        if status.lower() not in ["todo", "done", "pending"]:
            raise ValidationError(
                'invalid status value, status should be in ["todo","done","pending"]'
            )
        return status


class RegistrationForm(UserCreationForm):
    """
    registration form
    """

    email = forms.EmailField()
    birthDate = forms.DateField(
        widget=forms.TextInput(
            {"placeholder": "Enter your date of birth in yyyy-mm-dd format"}
        )
    )
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        """
        meta class for registration
        """

        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "birthDate",
        ]

    @override
    def clean_username(self):
        name: str = str(self.cleaned_data.get("username"))
        if "admin" in name or name == "admin":
            raise ValidationError("admin username not allowed")
        return name

    def clean_birthDate(self):
        birth_date = self.cleaned_data.get("birthDate")
        if not birth_date:
            raise ValidationError("enter valid date")
        if datetime.date.today().year - birth_date.year < 17:
            print("error raised")
            raise ValidationError("you are underage")
        return birth_date
