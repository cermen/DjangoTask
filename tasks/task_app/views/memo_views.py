from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from ..models import Task, Memo
from ..forms import MemoForm


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
def memo_modify(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.id = memo_id
            memo.modify_date = timezone.now()
            memo.save()
            return redirect('task_app:detail', task_id=memo.task.id)
    else:
        form = MemoForm(instance=memo)
    return render(request, 'task_app/memo_form.html', {'form': form})


@login_required(login_url='common:login')
def memo_delete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete()
    return redirect('task_app:detail', task_id=memo.task.id)


@login_required(login_url='common:login')
def memo_important(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.important = not memo.important
    memo.save()
    return redirect('task_app:detail', task_id=memo.task.id)
