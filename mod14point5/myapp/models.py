from django.db import models

# Create your models here.
class PracticeModelForm(models.Model):
    name = models.CharField(max_length=50)
    auto_field = models.AutoField(primary_key=True)
    email = models.EmailField()
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    generic_ip_address_field = models.GenericIPAddressField()
    # image_field = models.ImageField(upload_to='files/')
    json_field = models.JSONField()
    slug_field = models.SlugField()
    time_field = models.TimeField()
    url_field = models.URLField()