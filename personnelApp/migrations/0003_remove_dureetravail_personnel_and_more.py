# Generated by Django 5.0 on 2024-06-16 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnelApp', '0002_conge_dureetravail_salaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dureetravail',
            name='personnel',
        ),
        migrations.RemoveField(
            model_name='salaire',
            name='personnel',
        ),
        migrations.DeleteModel(
            name='Conge',
        ),
        migrations.DeleteModel(
            name='DureeTravail',
        ),
        migrations.DeleteModel(
            name='Salaire',
        ),
    ]
