from django.shortcuts import render, redirect, HttpResponse,  get_object_or_404 
from .forms import PersonnelRegistration
from .models import Utilisateur, Conge, Paiement
from django.db.models import Sum, F, Count
from django.db.models.functions import TruncMonth
from babel.dates import format_date
from datetime import date
#elle permet d'ajouter et d'afficher les infos

def add_show(request):
    if request.method == 'POST':
        form = PersonnelRegistration(request.POST)
        if form.is_valid():
            form.save()  # Cette ligne sauvegarde directement les données dans la base de données
            return redirect('add_show')  # Redirection vers la page d'affichage après ajout
    else:
        form = PersonnelRegistration()
    
    pers = Utilisateur.objects.all()
    return render(request, 'personnel/add_show.html', {'form': form, 'pers': pers})
#elle permet de supprimer les donnees
def delete_data(request, id):
    utilisateur = get_object_or_404(Utilisateur, pk=id)  # Récupère l'utilisateur ou renvoie une erreur 404
    if request.method == 'POST':
        utilisateur.delete()
        return redirect('add_show')
   #elle permet de modifier les donnees

def update_data(request, id):
    pi = get_object_or_404(Utilisateur, pk=id)
    if request.method == 'POST':
        fm = PersonnelRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('add_show')  # Rediriger vers la liste après la mise à jour
    else:
        fm = PersonnelRegistration(instance=pi)
    return render(request, 'personnel/modifier_personnel.html', {'form': fm, 'id': id})

def gerer_conge(request):
    if request.method == 'POST':
        form = FormulaireConge(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_conge')
    else:
        form = FormulaireConge()
    return render(request, 'personnel/gerer_conge.html', {'form': form})

def gerer_paiement(request):
    if request.method == 'POST':
        form = FormulairePaiement(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_paiement')
    else:
        form = FormulairePaiement()
    return render(request, 'personnel/gerer_paiement.html', {'form': form})

def liste_personnel(request):
    personnel = Utilisateur.objects.all()
    return render(request, 'personnel/liste_personnel.html', {'personnel': personnel})

def liste_conge(request):
    conges = Conge.objects.all()
    return render(request, 'personnel/liste_conge.html', {'conges': conges})

def liste_paiement(request):
    paiements_par_mois = Paiement.objects.values('utilisateur__nom', 'utilisateur__role', 'date__month', 'date__year').annotate(
        total_paiement=Sum('montant'),
        mois=F('date')
    ).order_by('date__year', 'date__month', 'utilisateur__nom')

    # Organiser les paiements par mois pour un affichage facile dans le template
    paiements_grouped = {}
    for paiement in paiements_par_mois:
        mois = date(paiement['date__year'], paiement['date__month'], 1)  # Créer un objet date pour le premier jour du mois
        mois_format = format_date(mois, format='MMMM yyyy', locale='fr')
        if mois_format not in paiements_grouped:
            paiements_grouped[mois_format] = []
        paiements_grouped[mois_format].append(paiement)

    return render(request, 'personnel/liste_paiement.html', {'paiements_grouped': paiements_grouped})

def accueil(request):
    total_employees = Utilisateur.objects.count()
    total_leaves = Conge.objects.count()
    total_payments = Paiement.objects.count()

    context = {
        'total_employees': total_employees,
        'total_leaves': total_leaves,
        'total_payments': total_payments,
    }
    return render(request, 'personnel/accueil.html', context) 