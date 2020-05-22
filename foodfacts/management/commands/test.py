import os
from django.core.management import BaseCommand


class Command(BaseCommand):
    """This command becomes available from manage.py"""

    help = "Executes project tests."

    def handle(self, *args, **options):
        os.system("pytest -v -rf")
