from django.shortcuts import render
from rest_framework import generics
from .models import Building, City
from .serializers import BuildingSerializer, CitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

# API views for Buildings
class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

# API views for Cities
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Optional: Create an API root view that points to both buildings and cities endpoints.
class APIRoot(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'buildings': reverse('building-list', request=request),
            'cities': reverse('city-list', request=request),
        })
