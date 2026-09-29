from typing import override

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task
from ..serializers import TaskSerializer


class APITest(APITestCase):
    @override
    def setUp(self) -> None:
        self.user = User.objects.create(username="john", password="12FWE#$1")
        self.task1 = {
            "title": "api test task",
            "description": "api test case",
            "status": "todo",
            "due_date": "2026-10-18",
        }

    def test_create_endpoint(self):
        self.client.force_login(user=self.user)

        response = self.client.post(
            reverse("tasks:taskList_api_view"), data=self.task1, format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_api_list(self):
        self.client.force_login(user=self.user)
        _ = self.client.post(
            reverse("tasks:taskList_api_view"), data=self.task1, format="json"
        )

        response = self.client.get(reverse("tasks:taskList_api_view"))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(response.json()[0]["title"], "api test task")
