from django.core.management.base import BaseCommand, CommandError
from notemanagement.models import Category

class Command(BaseCommand):
    help = 'Testing command for note management'

    def handle(self, *args, **options):
        cats = Category.objects.all()
        for cat in cats:
            self.stdout.write('Category: %s\n' % cat)
        self.stdout.write('DONE\n')