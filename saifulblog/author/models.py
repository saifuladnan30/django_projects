from django.db import models


# Create your models here.

# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     bio = models.TextField()
#     phone = models.CharField(max_length=15)

#     def __str__(self) -> str:
#         return f"{self.name}"

# # Create your models here.
# class Profile(models.Model):
#     name = models.CharField(max_length=50)
#     about = models.TextField()
#     author = models.OneToOneField(Author, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f"{self.name}"