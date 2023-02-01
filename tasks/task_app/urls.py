from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:task_id>', views.detail),
]
