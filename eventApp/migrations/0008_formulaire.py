# Generated by Django 5.0 on 2024-06-05 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0007_remove_project_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('service', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chemin_facture', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
