# Generated by Django 5.0 on 2024-06-04 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0004_category_alter_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
    ]
