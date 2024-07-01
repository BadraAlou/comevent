# myapp/management/commands/update_youtube_urls.py
from django.core.management.base import BaseCommand
from eventApp.models import Project

class Command(BaseCommand):
    help = 'Update YouTube URLs for existing projects'

    def handle(self, *args, **kwargs):
        projects = Project.objects.all()
        for project in projects:
            # Logique pour définir l'URL YouTube, par exemple:
            project.youtube_url = 'https://www.youtube.com/watch?v=example'
            project.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated YouTube URLs'))
