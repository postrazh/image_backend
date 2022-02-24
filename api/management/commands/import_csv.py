import codecs
import csv
from urllib import request

from django.core.management import BaseCommand

from api.models import Car

CSV_URL = 'https://docs.google.com/spreadsheets/d/1SYNFV6IGYOme9smQKVBFBPnOQvJa3MUi9QKGo2rFa94/pub?gid=0&single=true&output=csv'


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Removing the previous car data...')
        Car.objects.all().delete()

        print('Importing new car data...')

        # Fetch CSV file from online URL
        response = request.urlopen(CSV_URL)
        csv_rows = list(csv.DictReader(codecs.iterdecode(response, 'utf-8')))
        print(csv_rows)

        for row in csv_rows:
            car = Car.objects.create(**row)
            car.save()


