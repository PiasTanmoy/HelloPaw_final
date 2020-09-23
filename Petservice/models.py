from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    cost = models.CharField(max_length=20)

    def __str__(self):
        return self.name
