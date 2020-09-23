from django.db import models


# Create your models here.
class Payment(models.Model):
    amount = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.id