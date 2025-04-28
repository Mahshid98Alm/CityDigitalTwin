from django.contrib.gis.db import models

# Model for the Braga buildings table having the four specified columns.
class BragaBuildingFinal(models.Model):
    cluster_id = models.IntegerField(unique=True)
    height = models.FloatField()
    estimate_height = models.FloatField()
    geometry = models.GeometryField(srid=4326)  # Use the appropriate SRID

    def __str__(self):
        return f"Braga Cluster {self.cluster_id}"

    class Meta:
        managed = False  # Django will not manage (create/modify) this table.
        db_table = 'braga_buidings_final'


# Model for the Lisbon buildings table having the four specified columns.
class LisbonBuildingFinal(models.Model):
    cluster_id = models.IntegerField(unique=True)
    height = models.FloatField()
    estimate_height = models.FloatField()
    geometry = models.GeometryField(srid=4326)

    def __str__(self):
        return f"Lisbon Cluster {self.cluster_id}"

    class Meta:
        managed = False
        db_table = 'lisbon_buidings_final'
