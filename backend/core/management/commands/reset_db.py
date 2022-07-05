from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os

class Command(BaseCommand):
    help = "WARNING: RESET CURRENT DATABASE!"

    def handle(self, *args, **options):
        print("Deleting data from database...")
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "reset.sql")
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            cursor.execute(sql)