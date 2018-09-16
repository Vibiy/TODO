from django.contrib import admin
from .models import Task, TaskList


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'tasklist']


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList)
