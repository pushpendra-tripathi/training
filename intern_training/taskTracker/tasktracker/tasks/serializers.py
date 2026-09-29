import datetime
from pyexpat import model
from typing import override

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.db.models import fields_all
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "due_date", "owner"]

    @override
    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    @override
    def update(self, instance, validated_data):
        instance.title = validated_data.objects.get("title")
        instance.description = validated_data.objects.get("description")
        instance.status = validated_data.objects.get("status")
        instance.due_date = validated_data.objects.get("due_date")

        return instance

    @override
    def validate(self, attrs):
        today = datetime.date.today()
        max_date = today + relativedelta(months=1)
        deadline = attrs["due_date"]

        if attrs["status"] not in ["todo", "done", "pending"]:
            raise serializers.ValidationError(
                'status must be in ["todo","done","pending"]'
            )

        if deadline < today:
            raise serializers.ValidationError("due_date can't be in the past")
        elif deadline > max_date:
            print("max_date: ", max_date)
            print("today: ", today)
            raise serializers.ValidationError(
                "due_date can't be greater than 4 weeks from now"
            )
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    @override
    def validate(self, attrs):
        request = self.context.get("request")

        if not request or not request.user or not request.user.is_staff:
            raise serializers.ValidationError(
                "only admins are allowed to access this list"
            )

        return attrs
