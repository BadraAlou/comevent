# Generated by Django 5.0 on 2024-06-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0011_formulaire_duree'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDemande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
                ('services', models.CharField(choices=[('publicite', 'Publicité (prix: 50000 FCFA, durée: 1 mois)'), ('creation_digitale', 'Création digitale (prix: 75000 FCFA, durée: 2 mois)'), ('gestion_reseaux_sociaux', 'Gestion des réseaux sociaux (prix: 60000 FCFA, durée: 1 mois)')], max_length=50)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
