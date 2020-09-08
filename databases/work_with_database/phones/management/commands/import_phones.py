import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csv_file:

            phone_reader = csv.reader(csv_file, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                p = Phone(
                    id=line[0],
                    name=line[1],
                    image=line[2],
                    price=line[3],
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1]),
                )
                p.save()
                # TODO: Добавьте сохранение модели

