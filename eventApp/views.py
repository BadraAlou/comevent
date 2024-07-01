# main/views.py
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from xhtml2pdf import pisa
from .forms import SignUpForm, ContactForm, LoginForm, AppointmentForm
from .models import About, UserProfile, Formulaire, Service, Appointment, Client
from .models import Project, ProjectDetail, Contact
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, Image


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project_details = ProjectDetail.objects.filter(project=project)
    return render(request, 'project_detail.html', {'project': project, 'project_details': project_details})

# Informations de votre site
SITE_NAME = "COM.EVENT"
SITE_LOGO = settings.SITE_LOGO  # Utilisation de la variable définie dans settings.py
SITE_ADDRESS = "Bakodjikoroni Golf Rue : 14 , porte :356"
SITE_PHONE = "+223 60 02 32 56"
def home(request):
    clients = Client.objects.all()
    context = {
        'username': request.user.username,
        'clients': clients
    }
    return render(request, 'home.html', context)
    
def about(request):
    about_infos = About.objects.all()
    return render(request, 'about.html', {'about_infos': about_infos})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirige vers une page de confirmation
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def services(request):
    return render(request, 'services.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté avec succès.")
    return redirect('home')

def inscription(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Enregistre l'utilisateur
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                UserProfile.objects.create(
                    user=user,
                    prenom=form.cleaned_data.get('prenom'),
                    nom=form.cleaned_data.get('nom'),
                    email=email,
                    numero_telephone=form.cleaned_data.get('numero_telephone')
                )
                messages.success(request, f'Bienvenue, {user.first_name}! Votre compte a été créé avec succès.')
                return redirect('home')  # Redirige vers la page d'accueil après l'inscription
            else:
                messages.error(request, 'Erreur d\'authentification après la création du compte.')
        else:
            messages.error(request, 'Erreur dans le formulaire d\'inscription.')
    else:
        form = SignUpForm()
    return render(request, 'inscription.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Nom d’utilisateur ou mot de passe incorrect')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('appointment_success', pk=appointment.pk)
        else:
            messages.error(request, "Erreur dans le formulaire de rendez-vous.")
    else:
        form = AppointmentForm()
    
    services = Service.objects.all()
    return render(request, 'appointment_form.html', {'form': form, 'services': services})

def appointment_success(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointment_success.html', {'appointment': appointment})

def generate_pdf(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="appointment_{appointment.pk}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    styleH = styles['Heading1']
    styleN = styles['BodyText']
    styleB = styles['BodyText']
    styleB.fontName = 'Helvetica-Bold'

    # Create a table to hold the logo and the site information
    logo_data = []

    if SITE_LOGO:
        logo = Image(SITE_LOGO)
        logo.drawHeight = 50  # height of the logo
        logo.drawWidth = 100  # width of the logo
       

    # Create a table for the site info
    site_info_data = [
        [Paragraph(SITE_NAME, styleH)],
        [Paragraph(SITE_ADDRESS, styleN)],
        [Paragraph(f"Téléphone: {SITE_PHONE}", styleN)]
    ]

    site_info_table = Table(site_info_data, colWidths=[400])
    logo_data.append([logo, site_info_table])

    logo_table = Table(logo_data, colWidths=[100, 400])
    logo_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    elements.append(logo_table)
    elements.append(Spacer(1, 12))

    # Line
    line = Table(
        [['']],
        colWidths=[doc.width],
        style=TableStyle([
            ('LINEBELOW', (0, 0), (0, 0), 1, colors.black),
        ])
    )
    elements.append(line)
    elements.append(Spacer(1, 12))

    # Appointment Details
    elements.append(Paragraph(f"Rendez-vous ID: {appointment.pk}", styleB))
    elements.append(Spacer(1, 12))

    data = [
        ['Service:', appointment.service.name],
        ['Nom:', appointment.name],
        ['Email:', appointment.email],
        ['Téléphone:', appointment.phone],
        ['Date:', appointment.date.strftime('%d/%m/%Y')],
        ['Heure:', appointment.time.strftime('%H:%M')],
        ['Adresse:', appointment.address],
        ['Ville:', appointment.city],
    ]

    table = Table(data, colWidths=[100, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Build PDF
    doc.build(elements)

    return response

