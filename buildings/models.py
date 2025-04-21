import uuid
from django.db import models

# Create your models here.
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField(null=True, blank=True)  # Optional field

    def __str__(self):
        return self.name

class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=300, blank=True)
    # Relate a building to a city. Allow null if you don't always have a city.
    city = models.ForeignKey(City, related_name='buildings', on_delete=models.CASCADE, null=True, blank=True)
    geometry = models.JSONField(blank=True, null=True)
    osm_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name or str(self.id)
