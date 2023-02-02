from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
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


def memo_create(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.memo_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('task_app:detail', task_id=task.id)
