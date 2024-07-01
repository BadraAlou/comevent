# Generated by Django 5.0 on 2024-06-19 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnelApp', '0005_departement_role_utilisateur_adresse_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='departement',
        ),
        migrations.RemoveField(
            model_name='paiement',
            name='utilisateur',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='role',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='date_embauche',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Conge',
        ),
        migrations.DeleteModel(
            name='Departement',
        ),
        migrations.DeleteModel(
            name='Paiement',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
