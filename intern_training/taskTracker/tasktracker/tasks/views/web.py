from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.core.paginator import PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView

from ..forms import RegistrationForm, TaskForm
from ..models import Task


def Home(request):
    return render(request, "tasks/Home.html")


@login_required
def tasks_list(request):
    task_list = Task.objects.all().order_by("-created_at")
    title = request.GET.get("title")
    due_date = request.GET.get("due_date")
    owner = request.user

    if owner.is_superuser:
        task_list = Task.objects.all()
    elif title:
        task_list = task_list.filter(title__icontains=title)
    elif due_date:
        task_list = task_list.filter(due_date=due_date)
    elif owner:
        task_list = task_list.filter(owner=owner)
    paginator = Paginator(task_list, 5)

    try:
        page_num = request.GET.get("page")
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    else:
        page_obj = paginator.get_page(page_num)

    return render(request, "tasks/tasks.html", context={"pages": page_obj})


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)

    return render(request, "tasks/task_details.html", context={"task": task})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            form.save()
            messages.success(request, "task created successfully")
            return redirect("/tasks_lists")
        else:
            messages.error(
                request, "There was an error creating task, see below for more info"
            )
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", context={"form": form})


def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'task "{task.title}" was successfully updated')
            return redirect("/tasks_lists")
        else:
            messages.error(
                request,
                f'"{task.title}" task update failed, see below for more information',
            )
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", context={"form": form})


def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.delete()
        messages.success(request, f'"{task}" deleted successfully')
        return redirect("/tasks_lists")

    return render(request, "tasks/confirmation.html", {"task": task})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "tasks/register.html", {"form": form})


def about(request):
    return render(request, "tasks/about.html")
