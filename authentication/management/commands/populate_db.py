from django.core.management.base import BaseCommand
from pokemon_api.load_data import populate

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Populating the database with pokemons...')
        populate()
        self.stdout.write('Database successfuly populated!')
