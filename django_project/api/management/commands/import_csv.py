import codecs
import csv
from tempfile import NamedTemporaryFile
from urllib import request
from urllib.request import urlopen

from django.core.files import File
from django.core.management import BaseCommand

from api.models import Car

CSV_URL = 'https://docs.google.com/spreadsheets/d/1SYNFV6IGYOme9smQKVBFBPnOQvJa3MUi9QKGo2rFa94/pub?gid=0&single=true&output=csv'


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Removing the previous car data...')
        for car in Car.objects.all():
            car.delete()

        print('Importing new car data...')

        # Fetch CSV file from online URL
        try:
            response = request.urlopen(CSV_URL)
            csv_rows = list(csv.DictReader(codecs.iterdecode(response, 'utf-8')))
        except Exception:
            print('Can not pull the CSV file.')
            return

        print(csv_rows)

        for row in csv_rows:
            car = Car.objects.create(title=row.get('title'), description=row.get('description'),
                                     image_url=row.get('image'))

            print(f'----- Saving: {car} -----')
            car.get_image()
            car.save()

