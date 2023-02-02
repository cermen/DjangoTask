from django.db import models


# Create your models here
class Task(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class Memo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
