import  csv

from django.core.management.base import BaseCommand, CommandError
from foods.models import Ingredient


class Command(BaseCommand):
    """
    Загрузка ингредиентов в БД
    """
    help = 'Load ingredients'

    def handle(self, *args, **options):
        with open('foods/management/commands/ingredients.csv') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                Ingredient.objects.get_or_create(name=row[0], unit=row[1])
