from django.db.models import Count
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

from .models import Task, TaskGroup
from .forms import TaskModelForm, TaskGroupModelForm


class TaskGroupList(BaseCreateView, ListView):
    model = TaskGroup
    template_name = 'index.html'
    form_class = TaskGroupModelForm
    context_object_name = 'form'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(number_of_tasks=Count('task'))
        return qs


class TaskGroupItem(BaseCreateView, DetailView):
    queryset = TaskGroup.objects.prefetch_related('task_set__tags')
    template_name = 'detail.html'
    model = Task
    form_class = TaskModelForm
    context_object_name = 'form'

    def form_valid(self, form):
        form.instance.group = TaskGroup.objects.get(id=self.kwargs['pk'])
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('detail', kwargs=self.kwargs)
