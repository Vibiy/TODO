from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

from .models import Task, TaskGroup
from .forms import TaskModelForm, TaskGroupModelForm


class TaskGroupList(ListView):
    model = TaskGroup
    template_name = 'index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(number_of_tasks=Count('task'))
        return qs


class TaskGroupItem(DetailView):
    queryset = TaskGroup.objects.prefetch_related('task_set__tags')
    template_name = 'detail.html'


class TaskGroupCreate(CreateView):
    model = TaskGroup
    form_class = TaskGroupModelForm
    context_object_name = 'form'
    template_name = 'taskgroup_add.html'
    success_url = reverse_lazy('index')


class TaskCreate(CreateView):
    model = Task
    form_class = TaskModelForm
    context_object_name = 'form'
    template_name = 'task_add.html'

    def form_valid(self, form):
        form.instance.group = TaskGroup.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.group.id})
