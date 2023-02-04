from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from django.http import HttpResponseNotAllowed
from .forms import TaskForm, MemoForm


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
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.create_date = timezone.now()
            memo.task = task
            memo.save()
            return redirect('task_app:detail', task_id=task.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'task': task, 'form': form}
    return render(request, 'task_app/task_detail.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_app:index')
    else:
        form = TaskForm()
    return render(request, 'task_app/task_form.html', {'form': form})
