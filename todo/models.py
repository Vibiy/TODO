from django.db import models


class TaskGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TaskQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active=True)


class TaskManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tags')


class Task(models.Model):
    name = models.CharField(max_length=30)
    group = models.ForeignKey('todo.TaskGroup', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('todo.Tag', blank=True)
    active = models.BooleanField(default=False)
    objects = TaskQuerySet.as_manager()
    prefetched = TaskManager.from_queryset(TaskQuerySet)()

    def __str__(self):
        return self.name
