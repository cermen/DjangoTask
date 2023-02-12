from django.urls import path
from . import views

from .views import base_views, tasks_views, memo_views

app_name = 'task_app'


urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:task_id>/', base_views.detail, name='detail'),

    path('task/create/', tasks_views.task_create, name='task_create'),
    path('task/modify/<int:task_id>', tasks_views.task_modify, name='task_modify'),
    path('task/delete/<int:task_id>', tasks_views.task_delete, name='task_delete'),

    path('memo/create/<int:task_id>', memo_views.memo_create, name='memo_create'),
    path('memo/modify/<int:memo_id>', memo_views.memo_modify, name='memo_modify'),
    path('memo/delete/<int:memo_id>', memo_views.memo_delete, name='memo_delete')
]
