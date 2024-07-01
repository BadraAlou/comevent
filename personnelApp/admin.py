from django.contrib import admin
from .models import Utilisateur, Conge, Paiement, Departement, Role

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'departement', 'role', 'date_embauche', 'is_active')
    search_fields = ('nom', 'email', 'telephone')
    list_filter = ('departement', 'role', 'is_active')
    ordering = ('nom',)

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'date_debut', 'date_fin', 'raison', 'approuve')
    search_fields = ('utilisateur__nom', 'raison')
    list_filter = ('approuve', 'date_debut', 'date_fin')
    ordering = ('date_debut',)

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'montant', 'date', 'description')
    search_fields = ('utilisateur__nom', 'description')
    list_filter = ('date',)
    ordering = ('date',)

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)
    ordering = ('nom',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
    ordering = ('nom',)
