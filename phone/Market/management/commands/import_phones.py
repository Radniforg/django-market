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
                product = Product(name=line[0],
                              picture_link=line[1], information=line[2], category_id=line[3])
                product.save()
                # TODO: Добавьте сохранение модели


