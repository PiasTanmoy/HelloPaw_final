from django.db import models
from PetService.models import Service
from PetShop.models import Petshop


# Create your models here.
class Payment(models.Model):
    amount = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    S_id = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    P_id = models.ForeignKey(Petshop, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id