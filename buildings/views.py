from rest_framework.generics import ListAPIView
from .models import BragaBuildingFinal, LisbonBuildingFinal
from .serializers import BragaBuildingSerializer, LisbonBuildingSerializer

class BragaBuildingListView(ListAPIView):
    queryset = BragaBuildingFinal.objects.all()
    serializer_class = BragaBuildingSerializer

class LisbonBuildingListView(ListAPIView):
    queryset = LisbonBuildingFinal.objects.all()
    serializer_class = LisbonBuildingSerializer
