"""
URL configuration for cityDigitalTwin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def homepage(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>City Twin</title>
    </head>
    <body>
        <h1>Hello, Welcome to the Digital Twin system.</h1>
        <p>Available Endpoints:</p>
        <ul>
            <li><a href="/admin/">Admin Panel</a></li>
            <li><a href="/api/braga-buildings/">Braga Buildings API</a></li>
            <li><a href="/api/lisbon-buildings/">Lisbon Buildings API</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('buildings.urls')),  # Ensure buildings.urls maps to your Braga and Lisbon endpoints.
    path('', homepage, name='index'),
]
