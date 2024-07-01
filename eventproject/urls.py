from django.contrib.auth import views as auth_views  # Importer auth_views pour les vues d'authentification
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from eventApp import views as event_views  # Alias pour les vues de eventApp
from personnelApp import views as personnel_views  # Alias pour les vues de personnelApp


urlpatterns = [
    path('', event_views.home, name='home'),  # Utilisez event_views pour home
    
    path('admin/', admin.site.urls),
    path('about/', event_views.about, name='about'),
    path('portfolio.html', event_views.portfolio, name='portfolio_html'),
    path('services.html', event_views.services, name='services_html'),
    path('contact.html', event_views.contact, name='contact_html'),
    path('login/', event_views.login_view, name='login'),
    path('inscription/', event_views.inscription, name='inscription'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Utilisez auth_views.PasswordResetView
    path('logout/', event_views.logout_view, name='logout'),
    path('success/', event_views.success, name='success'),
    path('appointment/', event_views.appointment_view, name='appointment'),
    path('appointment/success/<int:pk>/', event_views.appointment_success, name='appointment_success'),
    path('appointment/pdf/<int:pk>/', event_views.generate_pdf, name='appointment_pdf'),
    path('appointment/form/', event_views.appointment_view, name='appointment_form'),
    path('project/<int:project_id>/', event_views.project_detail, name='project_detail'),
    path('personnel/', personnel_views.accueil, name='accueil'),  # Ajout de cette ligne pour la vue add_show
    path('personnel/delete/<int:id>/', personnel_views.delete_data, name='deletedata'),  
    path('personnel/update/<int:id>/', personnel_views.update_data, name='updatedata'),
    path('personnel/gerer-conge/', personnel_views.gerer_conge, name='gerer_conge'),
    path('personnel/gerer-paiement/', personnel_views.gerer_paiement, name='gerer_paiement'),
    path('personnel/liste-personnel/', personnel_views.liste_personnel, name='liste_personnel'),
    path('personnel/liste-conge/', personnel_views.liste_conge, name='liste_conge'),
    path('personnel/liste-paiement/', personnel_views.liste_paiement, name='liste_paiement'),
    path('personnel/add_show/', personnel_views.add_show, name='add_show'),  
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
