from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

from .models import Task, TaskGroup
from .forms import TaskModelForm, TaskGroupModelForm


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


class TaskGroupCreateView(CreateView):
    model = TaskGroup
    form_class = TaskGroupModelForm
    context_object_name = 'form'
    template_name = 'taskgroup_add.html'
    success_url = reverse_lazy('index')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskModelForm
    context_object_name = 'form'
    template_name = 'task_add.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})