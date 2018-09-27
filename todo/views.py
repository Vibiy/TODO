from django.db.models import Count
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, BaseCreateView
from django.urls import reverse, reverse_lazy

from .models import Task, TaskGroup
from .forms import TaskModelForm, TaskGroupModelForm


class TaskGroupCreateAndList(CreateView):
    model = TaskGroup
    template_name = 'index.html'
    form_class = TaskGroupModelForm
    context_object_name = 'form'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['task_group_list'] = TaskGroup.objects.all().annotate(number_of_tasks=Count('task'))
        return context


class TaskGroupCreateAndDetail(CreateView):
    model = Task
    template_name = 'detail.html'
    form_class = TaskModelForm
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        qs = TaskGroup.objects.prefetch_related('task_set__tags')
        context['group'] = qs.filter(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.group = TaskGroup.objects.get(id=self.kwargs['pk'])
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('detail', kwargs=self.kwargs)
