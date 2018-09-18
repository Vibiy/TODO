from django.shortcuts import render
from .models import Task, TaskGroup


def index(request):
    task_group_list = TaskGroup.objects.all()
    context = {'task_group_list': task_group_list}
    return render(request, "index.html", context)

def detail(request, pk):
    task_list = Task.objects.filter(group__id=pk)
    context = {'task_list': task_list}
    return render(request, "detail.html", context)
