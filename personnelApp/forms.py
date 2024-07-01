from django import forms
from .models import Utilisateur, Conge, Paiement, Departement, Role

class PersonnelRegistration(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'email', 'password', 'telephone', 'adresse', 'date_embauche', 'departement', 'role', 'is_active']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control'}),
            'date_embauche': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'departement': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class FormulaireConge(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['utilisateur', 'date_debut', 'date_fin', 'raison', 'approuve']
        widgets = {
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'raison': forms.TextInput(attrs={'class': 'form-control'}),
            'approuve': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class FormulairePaiement(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['utilisateur', 'montant', 'date', 'description']
        widgets = {
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
