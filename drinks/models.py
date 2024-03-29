from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name + ' ' + self.description
