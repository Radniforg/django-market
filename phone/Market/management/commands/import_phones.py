import csv

from django.core.management.base import BaseCommand
from Market.models import Product, Category


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                product = Product(id=line[0], name=line[1],
                              image=line[2], information=line[3], category_id=line[4])
                product.save()
                # TODO: Добавьте сохранение модели


