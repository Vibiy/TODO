from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.TaskGroupList.as_view(), name='index'),
    path('detail/<int:pk>/', views.TaskGroupItem.as_view(), name='detail'),
    path('add_group_task', views.TaskGroupCreate.as_view(), name='add-group'),
    path('detail/<int:pk>/add_task', views.TaskCreate.as_view(), name='add-task'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
