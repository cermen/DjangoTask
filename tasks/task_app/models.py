from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Memo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
