from django.db import models

# Create your models here.

class Petshop(models.Model):
    
    name = models.CharField(max_length=30)
    cost = models.FloatField()

    def __str__(self):
        return self.name
