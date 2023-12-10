from django.db import models
from category.models import TaskCategory
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    TaskAssignDate = models.DateField()
    task_category = models.ManyToManyField(TaskCategory)

    def __str__(self) -> str:
        return self.taskTitle