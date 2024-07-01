# Generated by Django 5.0 on 2024-06-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('poste', models.CharField(max_length=100)),
                ('date_embauche', models.DateField()),
            ],
        ),
    ]
