from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class TodoList(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.id

class Todo(models.Model):
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    finished_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_finished = models.BooleanField(default=False, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.id
