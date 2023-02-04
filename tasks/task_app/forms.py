from django import forms
from .models import Task, Memo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': '할일',
            'start_date': '시작일',
            'end_date': '종료일'
        }


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'content': '메모하기'
        }
