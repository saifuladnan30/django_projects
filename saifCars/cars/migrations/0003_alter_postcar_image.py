# Generated by Django 4.2.7 on 2023-12-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_postcar_image_remove_postcar_brand_postcar_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
