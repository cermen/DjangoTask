from django.urls import path
from . import views


app_name = 'task_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
]
