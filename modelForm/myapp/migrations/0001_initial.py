# Generated by Django 4.2.7 on 2023-12-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=5)),
                ('address', models.TextField()),
            ],
        ),
    ]
