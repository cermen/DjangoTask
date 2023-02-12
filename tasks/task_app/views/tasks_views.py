from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Task
from ..forms import TaskForm


@login_required(login_url='common:login')
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('task_app:index')
    else:
        form = TaskForm()
    return render(request, 'task_app/task_form.html', {'form': form})


@login_required(login_url='common:login')
def task_modify(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.id = task_id
            task.author = request.user
            task.save()
            return redirect('task_app:detail', task_id=task.id)
    else:
        form = TaskForm()
    return render(request, 'task_app/task_form.html', {'form': form})


@login_required(login_url='common:login')
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_app:index')
