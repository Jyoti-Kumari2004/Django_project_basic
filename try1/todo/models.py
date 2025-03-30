from django.db import models

# Create your models here.
class TodoItem(models.Model):
    task_domain=models.CharField(max_length=100)
    task_description=models.TextField()
    task_due_date=models.DateField()