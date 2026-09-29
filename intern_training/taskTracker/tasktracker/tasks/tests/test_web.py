from typing import override

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Task


class AuthTest(TestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(
            username="testuser1", password="1X<ISRUkw+tuK"
        )
        self.test_user2 = User.objects.create_user(
            username="testuser2", password="2HJ1vRV0Z&3iD"
        )

        self.task1 = Task.objects.create(
            title="Buy groceries",
            description="Milk and bread",
            due_date="2026-09-12",
            owner=self.test_user1,
        )
        self.task2 = Task.objects.create(
            title="Buy milk",
            description="Milk and bread",
            due_date="2026-09-12",
            owner=self.test_user2,
        )

    def test_login_redirect(self):
        respose = self.client.get(reverse("tasks:tasks_list"))
        self.assertRedirects(respose, "/accounts/login/?next=/tasks/tasks_lists/")

    def test_logged_in_uses_correct_template_for_tasks_list(self):
        login = self.client.login(username="testuser1", password="1X<ISRUkw+tuK")

        response = self.client.get(reverse("tasks:tasks_list"))

        self.assertEqual(str(response.context["user"]), "testuser1")
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed("tasks/tasks.html")

    def test_for_user_scoped_view(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse("tasks:tasks_list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context["user"]), "testuser1")
        self.assertContains(response, "Buy groceries")


class TaskUpdateAndDelete(TestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(
            username="testuser1", password="1X<ISRUkw+tuK"
        )
        self.test_user2 = User.objects.create_user(
            username="testuser2", password="2HJ1vRV0Z&3iD"
        )
        self.task1 = Task.objects.create(
            title="Buy groceries",
            description="Milk and bread",
            due_date="2026-10-21",
            owner=self.test_user1,
        )
        self.task2 = Task.objects.create(
            title="Plan trip",
            description="Book hotel",
            due_date="2026-10-20",
            owner=self.test_user1,
        )
        self.task2 = Task.objects.create(
            title="Write report",
            description="Draft summary",
            due_date="2026-10-18",
            owner=self.test_user1,
        )

    def test_update_task(self):
        self.client.force_login(self.test_user1)
        response = self.client.post(
            reverse("tasks:update_task", kwargs={"pk": self.task1.id}),
            {
                "title": "Buy apples",
                "description": "Milk and bread",
                "due_date": "2026-10-18",
                "status": "todo",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Buy apples")

    def test_delete_task(self):
        self.client.force_login(self.test_user1)
        response = self.client.delete(
            reverse("tasks:delete_task", kwargs={"pk": self.task1.id})
        )

        self.assertEqual(response.status_code, 200)


class TasksListFilterTests(TestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(
            username="testuser1", password="1X<ISRUkw+tuK"
        )
        self.test_user2 = User.objects.create_user(
            username="testuser2", password="2HJ1vRV0Z&3iD"
        )
        Task.objects.create(
            title="Buy groceries",
            description="Milk and bread",
            due_date="2026-10-21",
            owner=self.test_user1,
        )
        Task.objects.create(
            title="Plan trip",
            description="Book hotel",
            due_date="2026-10-20",
            owner=self.test_user2,
        )
        Task.objects.create(
            title="Write report",
            description="Draft summary",
            due_date="2026-10-18",
            owner=self.test_user2,
        )

    def test_title_search_filters_tasks(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse("tasks:tasks_list"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Plan trip")
        self.assertContains(response, "Buy groceries")

    def test_due_date_filter_filters_tasks(self):
        self.client.force_login(self.test_user2)
        response = self.client.get(reverse("tasks:tasks_list"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Buy groceries")
        self.assertContains(response, "Write report")
        self.assertContains(response, "Plan trip")
