from django.shortcuts import render
from django.urls import reverse

def homepage(request):
    # Build URLs for our named endpoints.
    admin_url = reverse('admin:index')                      # Django admin panel URL.
    braga_buildings = reverse('braga_buildings')              # URL for the Braga Buildings API.
    lisbon_buildings = reverse('lisbon_buildings')            # URL for the Lisbon Buildings API.

    context = {
        'admin_url': admin_url,
        'braga_buildings': braga_buildings,
        'lisbon_buildings': lisbon_buildings,
    }
    return render(request, 'index.html', context)
