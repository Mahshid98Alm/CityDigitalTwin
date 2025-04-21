from django.urls import path
from .views import (APIRoot,
    BuildingListCreateView,
    BuildingDetailView,
    CityListCreateView,
    CityDetailView,)

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    
    # Building endpoints
    path('buildings/', BuildingListCreateView.as_view(), name='building-list'),
    path('buildings/<uuid:pk>/', BuildingDetailView.as_view(), name='building-detail'),
    
    # City endpoints
    path('cities/', CityListCreateView.as_view(), name='city-list'),
    path('cities/<uuid:pk>/', CityDetailView.as_view(), name='city-detail'),
]