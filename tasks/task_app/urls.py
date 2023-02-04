from django.urls import path
from . import views


app_name = 'task_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('memo/create/<int:task_id>', views.memo_create, name='memo_create')
]
