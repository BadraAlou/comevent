# Generated by Django 5.0 on 2024-06-04 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0006_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
