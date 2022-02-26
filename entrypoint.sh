#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

python manage.py import_csv

gunicorn image_backend.wsgi:application --bind 0.0.0.0:8000

