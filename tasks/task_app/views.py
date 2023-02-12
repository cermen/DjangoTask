from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm, MemoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='common:login')
def index(request):
    page = request.GET.get('page', '1')
    task_list = Task.objects.filter(author=request.user.id).order_by('id')
    paginator = Paginator(task_list, 15)
    page_obj = paginator.get_page(page)
    context = {'task_list': page_obj}
    return render(request, 'task_app/task_list.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    return render(request, 'task_app/task_detail.html', context)


@login_required(login_url='common:login')
def memo_create(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.author = request.user
            memo.create_date = timezone.now()
            memo.task = task
            memo.save()
            return redirect('task_app:detail', task_id=task.id)
    else:
        form = MemoForm()
    context = {'task': task, 'form': form}
    return render(request, 'task_app/task_detail.html', context)


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
