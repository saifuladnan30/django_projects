from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=5)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Roll: {self.roll} - {self.name}"