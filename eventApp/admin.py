from django.contrib import admin
from .models import UserProfile, Project, Formulaire, Appointment, Service, ProjectDetail, Client, Contact

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Formulaire)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(ProjectDetail)
admin.site.register(Client)
admin.site.register(Contact)
