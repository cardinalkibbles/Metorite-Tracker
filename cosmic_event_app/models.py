from django.db import models
from users_app import CustomUser

# Create your models here.


class CosmicEvent(models.Model):
    mass = models.DecimalField(max_digits=None, decimal_places=4)
    found = models.BooleanField()
    year = models.DateTimeField()
    latitude = models.DecimalField(max_digits=None, decimal_places=6)
    longitude = models.DecimalField(max_digits=None, decimal_places=6)
    user = models.ForeignKey(CustomUser)
