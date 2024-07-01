from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Formulaire
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M'),
        input_formats=['%H:%M'],
        label='Heure'
    )
    
    class Meta:
        model = Appointment
        fields = [
            'service', 'name', 'email', 'phone', 'date', 'time', 
            'address', 'city', 
        ]
        labels = {
            'service': 'Service',
            'name': 'Nom',
            'email': 'E-mail',
            'phone': 'Téléphone',
            'date': 'Date',
            'time': 'Heure',
            'address': 'Adresse',
            'city': 'Ville',
           
        }
        error_messages = {
            'name': {
                'required': 'Ce champ est obligatoire.',
            },
            'email': {
                'required': 'Ce champ est obligatoire.',
                'invalid': 'Veuillez entrer une adresse e-mail valide.',
            },
            # Ajoutez d'autres messages d'erreur personnalisés si nécessaire
        }

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

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        label="Nom d'utilisateur", 
    )
    password = forms.CharField(
        widget=forms.PasswordInput, 
        label="Mot de passe", 
    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']