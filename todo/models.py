from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    tasklist = models.ForeignKey('todo.TaskList', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TaskList(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
