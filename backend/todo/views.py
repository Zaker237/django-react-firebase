from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (
    TodoList,
    Todo,
)
from .serializers import (
    TodoListSerializer,
    TodoSerializer,
)


class TodoListListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the todolist items.
        """
        todolists = TodoList.objects.all()
        serializer = TodoListSerializer(todolists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the TodoList with given todolist data
        """

        data = {
            "title": request.data.get("title"),
            "created_at": request.data.get("created_at"),
            "creator": request.user.id,
        }
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoListDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self, todolist_id):
        """
        Helper method to get the object with given todolist_id
        """
        try:
            return TodoList.objects.get(id=todolist_id)
        except TodoList.DoesNotExist:
            return None# 3. Retrieve
    def get(self, request, todolist_id, *args, **kwargs):
        """
        Retrieves the TodoList with given todolist_id
        """
        todolist_instance = self.get_object(todolist_id, request.user.id)
        if not todolist_instance:
            return Response(
                {"res": "Object with todolist id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TodoListSerializer(todolist_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, todolist_id, *args, **kwargs):
        """
        Updates the todolist item with given todolist_id if exists
        """
        todolist_instance = self.get_object(todolist_id, request.user.id)
        if not todolist_instance:
            return Response(
                {"res": "Object with todolist id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            "title": request.data.get("title"),
            "created_at": request.data.get("created_at"),
            "creator": request.user.id,
        }
        serializer = TodoListSerializer(instance = todolist_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, todolist_id, *args, **kwargs):
        """
        Deletes the todolist item with given todolist_id if exists
        """
        todolist_instance = self.get_object(todolist_id, request.user.id)
        if not todolist_instance:
            return Response(
                {"res": "Object with todolist id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todolist_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the todo items.
        """
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the Todo with given todo data
        """
        data = {
            "description": request.data.get("description"),
            "created_at": request.data.get("created_at"),
            "finished_at": request.data.get("finished_at"),
            "is_finished": request.data.get("is_finished"),
            "creator": request.user.id,
            "todolist": request.data.get("todolist"),
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]
    def get_object(self, todo_id):
        """
        Helper method to get the object with given todo_id
        """
        try:
            return Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return None# 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        """
        Retrieves the Todo with given todo_id
        """
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        """
        Updates the todo item with given todo_id if exists
        """
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            "description": request.data.get("description"),
            "created_at": request.data.get("created_at"),
            "finished_at": request.data.get("finished_at"),
            "is_finished": request.data.get("is_finished"),
            "creator": request.user.id,
            "todolist": request.data.get("todolist"),
        }
        serializer = TodoSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        """
        Deletes the todo item with given todo_id if exists
        """
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
