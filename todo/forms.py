from django.forms import ModelForm

from .models import Task, TaskGroup


class TaskModelForm(ModelForm):

    class Meta:
        model = Task
        exclude = ['group']


class TaskGroupModelForm(ModelForm):

    class Meta:
        model = TaskGroup
        exclude = []
