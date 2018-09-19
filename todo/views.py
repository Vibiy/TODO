from django.views.generic.list import ListView

from .models import Task, TaskGroup


class TaskGroupListView(ListView):
    model = TaskGroup
    context_object_name = 'task_group_list'
    template_name = 'index.html'


class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'detail.html'

    def get_queryset(self):
        context = Task.objects.filter(group=self.kwargs['pk'])
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TaskGroup.objects.get(id=self.kwargs['pk']).name
        return context