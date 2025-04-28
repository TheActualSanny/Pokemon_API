from django.core.management.base import BaseCommand
from django.db import connections
from time import sleep

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Checking database connection...')
        db_running = False
        while not db_running:
            try:
                connections['default'].cursor()
                db_running = True
            except:
                self.stdout.write('Not connected! Retrying...')
                sleep(3)
        self.stdout.write('Database is set up. Migrating...')