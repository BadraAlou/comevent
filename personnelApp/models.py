from django.db import models

# Create your models here.

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

class Role(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)
    date_embauche = models.DateField(null=True, blank=True)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Conge(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    raison = models.CharField(max_length=255)
    approuve = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.utilisateur.nom} - {self.date_debut} au {self.date_fin}'

class Paiement(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    montant = models.IntegerField()  # Utilisation de IntegerField pour éviter les chiffres à virgule
    date = models.DateField()  # Date du paiement

    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.utilisateur.nom} - {self.montant} CFA"