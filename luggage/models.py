# import uuid

from django.contrib.auth.models import User
from django.db import models


class Luggage(models.Model):
    # luggage_id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)

    passenger = models.ForeignKey(User, on_delete=models.CASCADE)

    status1 = models.BooleanField()
    status2 = models.BooleanField()
    status3 = models.BooleanField()
    status4 = models.BooleanField()

    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.pk)


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    n = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
