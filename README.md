# About
A Django app  which can be used to load data from a CSV and expose the data as an API using the Django Rest Framework.

# Set up
```shell
cd path/to/image_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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
## Get all cars
```shell
curl --location --request GET 'http://127.0.0.1:8000/api/cars'
```
```json
[
    {
        "id": 1,
        "image": "http://farm4.staticflickr.com/3764/10438039923_2ef6f68348_c.jpg",
        "title": "Item 1",
        "description": "Description 1"
    },
    ...
]
```

