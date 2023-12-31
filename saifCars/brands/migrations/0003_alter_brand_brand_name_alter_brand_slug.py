# Generated by Django 4.2.7 on 2023-12-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_alter_brand_brand_name_alter_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
