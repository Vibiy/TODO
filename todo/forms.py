from django import forms

from .models import Task, TaskGroup


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task


class TaskGroupModelForm(forms.ModelForm):
    class Meta:
        model = TaskGroup
