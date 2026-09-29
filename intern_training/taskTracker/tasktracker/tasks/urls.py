from django.urls import path

from .views import api, web

app_name = "tasks"
urlpatterns = [
    path("", web.Home, name="Home"),
    path("tasks_lists/", web.tasks_list, name="tasks_list"),
    path("about/", web.about, name="about"),
    path("create/", web.task_create, name="create_task"),
    path("update/<int:pk>", web.task_update, name="update_task"),
    path("delete/<int:pk>/", web.task_delete, name="delete_task"),
    path("task_details/<int:pk>", web.task_detail, name="task_details"),
    path("register", web.register, name="user_register"),
    path(route="api/taskslist", view=api.TaskListApiView, name="taskList_api_view"),
    path(
        route="api/taskdetail/<int:pk>",
        view=api.taskDetailApiView,
        name="taskdetail_api_view",
    ),
    path(route="users/", view=api.userList, name="user_list_view"),
]
