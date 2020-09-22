from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=20)
    pet_type = models.CharField(max_length=10)

    def __str__(self):
        return self.name

