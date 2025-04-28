from django.core.management.base import BaseCommand
from api.models import Pokemon
from pokemon_api.load_data import populate

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Checking the pokemons...')
        try:
            Pokemon.objects.all()[0]
            self.stdout.write('Database already populated!')
        except: 
            self.stdout.write('Populating the database...')
            populate()
            self.stdout.write('Database successfuly populated!')
