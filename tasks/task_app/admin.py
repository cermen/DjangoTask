from django.contrib import admin
from .models import Task, Memo

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']


class MemoAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Task, TaskAdmin)
admin.site.register(Memo, MemoAdmin)
