import uuid

from django.contrib.auth.models import User
from django.db import models


class Luggage(models.Model):
    luggage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)

    is_status1 = models.BooleanField()
    is_status2 = models.BooleanField()
    is_status3 = models.BooleanField()
    is_status4 = models.BooleanField()

    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.luggage_id)
