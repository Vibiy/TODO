from django.db.models import Count, Prefetch
from django.views.generic.edit import CreateView
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
        context = super().get_context_data(**kwargs)
        context['task_group_list'] = TaskGroup.objects.annotate(number_of_tasks=Count('task'))
        return context


class TaskGroupCreateAndDetail(CreateView):
    model = Task
    template_name = 'detail.html'
    form_class = TaskModelForm
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Task.objects.active().prefetch_related('tags')
        context['group'] = TaskGroup.objects\
            .prefetch_related(Prefetch('task_set', queryset=qs))\
            .get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.group = TaskGroup.objects.get(id=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs=self.kwargs)
