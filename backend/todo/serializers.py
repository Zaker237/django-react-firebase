from rest_framework import serializers
from .models import (
    TodoList,
    Todo,
)


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["title","created_at","creator",]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["description","created_at","finished_at","is_finished","creator","todolist",]
