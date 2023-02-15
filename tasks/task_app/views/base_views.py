from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from ..models import Task


@login_required(login_url='common:login')
def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    task_list = Task.objects.filter(author=request.user.id).order_by('id')
    if kw:
        task_list = task_list.filter(
            Q(title__icontains=kw)
        ).distinct()
    paginator = Paginator(task_list, 15)
    page_obj = paginator.get_page(page)
    context = {'task_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'task_app/task_list.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    return render(request, 'task_app/task_detail.html', context)
