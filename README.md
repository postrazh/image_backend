# About
A Django app  which can be used to load data from a CSV and expose the data as an API using the Django Rest Framework.

# Set up
```shell
cd path/to/image_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Migrate database
Given that the virtualenv had been set up and activated
```shell
python manage.py makemigrations
python manage.py migrate
```

# Load data
The app comes with a command to load in data from the path to a CSV file. An example usage with the test CSV file:
```shell
cd path/to/image_backend
python manage.py import_csv
```

# Run local server
Given that the virtualenv had been set up and activated
```shell
cd path/to/image_backend
python manage.py runserver
```

# REST APIs
## Get all cars without specifying a platform
```shell
curl --location --request GET 'http://127.0.0.1:8000/api/cars/'
```
```json
[
    {
        "id": 377,
        "title": "Item 1",
        "description": "Description 1",
        "image": null
    },
    {
        "id": 378,
        "title": "Item 2",
        "description": "Description 2",
        "image": "http://127.0.0.1:8000/media/CACHE/images/images/image_378/c98dd104e7926f6bf7f7f4d178a055da.jpg"
    },
    ...
]
```

## Get all cars for web platform
```shell
curl --location --request GET 'http://127.0.0.1:8000/api/cars/web/'
```

## Get all cars for mobile platform
```shell
curl --location --request GET 'http://127.0.0.1:8000/api/cars/mobile/'
```

# Design Considerations
1. To optimize the performance, CSV file needs to be imported earlier before REST API is requested.
2. For image caching, `imagekit`'s [default caching backend](https://django-imagekit.readthedocs.io/en/latest/caching.html) is used.
3. Various exceptions are handled properly especially when importing the csv file. Exception handling covers
   * invalid URL of the CSV file and failure of requesting it.
   * invalid URL of item images and failure of them.
   * valid URL of item image but invalid image content.
4. Support multiple working environments(development/staging/production).
   * Split the settings for each environment.
   * Use `.env` file for extracting out the sensitive information.
   * Use `docker-compose` for production deployment.

# Future roadmap
* Use AWS S3 backend and cloundfront domain in production deployment
* Use K8 for scaling the service.
* Use celery tasks for synchronizing importing CSV URL in real time.
* Use elastic search for better UX
