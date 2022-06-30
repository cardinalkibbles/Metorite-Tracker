from django.db import models
from users_app.models import CustomUser

# Create your models here.


class CosmicEvent(models.Model):
    name = models.CharField(max_length=45)
    mass = models.DecimalField(max_digits=500, decimal_places=4)
    found = models.BooleanField()
    date = models.DateField()
    latitude = models.DecimalField(max_digits=500, decimal_places=6)
    longitude = models.DecimalField(max_digits=500, decimal_places=6)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
