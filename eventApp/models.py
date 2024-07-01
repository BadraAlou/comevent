from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse



class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)  # Permettre des valeurs nulles temporairement
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.name} - {self.service.name} on {self.date} at {self.time}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    numero_telephone = models.CharField(max_length=15)

    def _str_(self):
        return f"{self.prenom} {self.nom}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name} - {self.created_at}"

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    prenom = forms.CharField(max_length=30, required=True)
    nom = forms.CharField(max_length=30, required=True)
    numero_telephone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'prenom', 'nom', 'email', 'numero_telephone', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']
        if commit:
            user.save()
        return user



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    youtube_url = models.URLField(max_length=200, default='')
    
    def __str__(self):
        return self.title


class Formulaire(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    message = models.TextField()
    service = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    chemin_facture = models.CharField(max_length=255, blank=True)
    duree = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nom} - {self.service}"

    def telecharger_facture_url(self):
        return reverse('telecharger_facture', args=[self.id])

def votre_vue(request):
    # Code pour récupérer le formulaire, par exemple :
    formulaire = Formulaire.objects.get(id=1)  # Remplacez cela par la logique pour récupérer le bon formulaire
    
    return render(request, 'formulaire.html', {'formulaire': formulaire})

class ProjectDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    detail_title = models.CharField(max_length=100)
    detail_description = models.TextField()
    detail_image = models.ImageField(upload_to='project_detail_images/')
    

    def __str__(self):
        return self.detail_title

class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clients_logos/')  # Assurez-vous que Pillow est installé

    def __str__(self):
        return self.name        

class VotreModele(models.Model):
    champ = models.CharField(max_length=100, default='valeur_par_defaut')        