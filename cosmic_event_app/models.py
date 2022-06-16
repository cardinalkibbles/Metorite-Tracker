from django.db import models
from users_app.models import CustomUser

# Create your models here.


class CosmicEvent(models.Model):
    mass = models.DecimalField(max_digits=50, decimal_places=4)
    found = models.BooleanField()
    year = models.DateTimeField()
    latitude = models.DecimalField(max_digits=50, decimal_places=6)
    longitude = models.DecimalField(max_digits=50, decimal_places=6)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
