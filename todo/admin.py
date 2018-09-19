from django.contrib import admin

from .models import Task, TaskGroup, Tag


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'created', 'modified']


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskGroup)
admin.site.register(Tag)
