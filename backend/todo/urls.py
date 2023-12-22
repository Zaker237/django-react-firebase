from django.urls import path
from .views import (
    TodoListListApiView,
    TodoListDetailApiView,
    TodoListApiView,
    TodoDetailApiView,
)

urlpatterns = [
    path("todolists", TodoListListApiView.as_view()),
    path("todolists/<int:todolist_id>/", TodoListDetailApiView.as_view()),
    path("todos", TodoListApiView.as_view()),
    path("todos/<int:todo_id>/", TodoDetailApiView.as_view()),
]