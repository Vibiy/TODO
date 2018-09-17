from django.shortcuts import render
from .models import Task, TaskList


def index(request):
    tasklist = TaskList.objects.all()
    context = {'tasklist': tasklist}
    return render(request, "index.html", context)

def detail(request, pk):
    tasklist = Task.objects.filter(tasklist__id=pk)
    listname = TaskList.objects.get(id=pk).name
    context = {'tasklist': tasklist, 'listname': listname}
    return render(request, "detail.html", context)
