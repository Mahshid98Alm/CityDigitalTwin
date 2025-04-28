from django.urls import path
from .views import BragaBuildingListView, LisbonBuildingListView

urlpatterns = [
    path('braga-buildings/', BragaBuildingListView.as_view(), name='braga_buildings'),
    path('lisbon-buildings/', LisbonBuildingListView.as_view(), name='lisbon_buildings'),
]
