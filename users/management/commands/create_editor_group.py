from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create Editor group'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Editors')
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created the Editors group'))
        else:
            self.stdout.write(self.style.SUCCESS('Editors group already exists'))
