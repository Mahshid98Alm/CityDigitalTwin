from django.shortcuts import render
from django.urls import reverse

def homepage(request):
    # Use reverse() to build URLs to named endpoints.
    # Make sure these names match what you set in your API URL configuration and admin.
    api_root = reverse('api-root')              # Our API root view (defined in buildings/urls.py)
    building_list = reverse('building-list')      # Endpoint for listing/creating buildings
    city_list = reverse('city-list')              # Endpoint for listing/creating cities
    admin_url = reverse('admin:index')            # Django admin panel’s URL

    context = {
        'api_root': api_root,
        'building_list': building_list,
        'city_list': city_list,
        'admin_url': admin_url,
    }
    return render(request, 'index.html', context)