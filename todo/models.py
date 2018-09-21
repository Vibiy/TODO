from django.db import models


class TaskGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=30)
    group = models.ForeignKey('todo.TaskGroup', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('todo.Tag', blank=True)

    def __str__(self):
        return self.name
