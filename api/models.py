from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    user_type = models.BooleanField()

class Warehouse(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}: {self.name}: {self.location}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
