from django.db import models
from PetShop.models import Petshop
from PetService.models import Service
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=20)
    pet_type = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class CustomerProduct(models.Model):
    c_id = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)
    p_id = models.ForeignKey(Petshop, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Customer.name + " : " + self.Petshop.name

class CustomerService(models.Model):
    c_id = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    s_id = models.ForeignKey(Service,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.Customer.name + " : " + self.Service.name

