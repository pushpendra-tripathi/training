from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser

from ..models import Task
from ..serializers import TaskSerializer, UserSerializer


@csrf_exempt
@api_view(["GET", "POSt"])
# @api_view(["POST"])
def TaskListApiView(request):
    """
    list all tasks and create
    """
    authentication_classes = {SessionAuthentication}
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    paginator = PageNumberPagination()
    paginator.page_size = 5

    if request.method == "GET":
        tasks = Task.objects.filter(owner=request.user).order_by("-created_at")
        if request.user.is_superuser:
            tasks = Task.objects.all()
        result_page = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def taskDetailApiView(request, pk):
    """
    test for update and delete
    """
    authentication_classes = {SessionAuthentication}
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    paginator = PageNumberPagination()
    paginator.page_size = 5
    try:
        task = Task.objects.get(pk=pk)
    except task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        tasks = Task.objects.filter(owner=request.user).order_by("-created_at")
        if request.user.is_superuser:
            tasks = Task.objects.all()
        result_page = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        task.delete()
        return HttpResponse(status=204)


def userList(request):
    Authentication_classes = {SessionAuthentication}
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticatedOrReadOnly,
    ]
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
