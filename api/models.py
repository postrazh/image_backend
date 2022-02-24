from django.db import models


class Car(models.Model):
    image = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
