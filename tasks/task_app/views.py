from django.shortcuts import render, get_object_or_404
from .models import Task


# Create your views here.
def index(request):
    task_list = Task.objects.order_by('id')
    context = {'task_list': task_list}
    return render(request, 'task_app/task_list.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    return render(request, 'task_app/task_detail.html', context)
