"""
URL configuration for tasktracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("__reload__/", include("django_browser_reload.urls")),
    path("tasks/", include("tasks.urls")),
    path("", include("tasks.urls")),
    path("about/", include("tasks.urls")),
    path("task_create", include("tasks.urls")),
    path("task_update", include("tasks.urls")),
    path("task_delete", include("tasks.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", include("tasks.urls")),
    path(route="api/taskslist", view=include(arg="tasks.urls")),
    path(route="api/taksdetail", view=include(arg="tasks.urls")),
    path(route="users/", view=include("tasks.urls")),
    path(route="api/auth-", view=include("rest_framework.urls")),
]
