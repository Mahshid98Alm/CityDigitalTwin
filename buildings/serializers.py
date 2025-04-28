from rest_framework_gis.serializers import GeoFeatureModelSerializer # type: ignore
from .models import BragaBuildingFinal, LisbonBuildingFinal

class BragaBuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BragaBuildingFinal
        geo_field = 'geometry'
        fields = ('cluster_id', 'height', 'estimate_height')  # Adjust as needed

class LisbonBuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LisbonBuildingFinal
        geo_field = 'geometry'
        fields = ('cluster_id', 'height', 'estimate_height')
