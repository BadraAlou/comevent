# Generated by Django 5.0 on 2024-06-07 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0018_alter_appointment_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotreModele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
    ]
