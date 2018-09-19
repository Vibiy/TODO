from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.TaskGroupListView.as_view(), name='index'),
    path('detail/<int:pk>/', views.TaskListView.as_view(), name='detail'),
    path('add_group_task', views.TaskGroupCreateView.as_view(), name='add-group'),
    path('detail/<int:pk>/add_task', views.TaskCreateView.as_view(), name='add-task'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns