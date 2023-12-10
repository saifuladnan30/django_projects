from django.db import models
from musician.models import Musician
# from category.models import TaskCategory

# Create your models here.
class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.album_name