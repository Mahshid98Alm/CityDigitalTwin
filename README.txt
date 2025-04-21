City Digital Twin Project
==========================

Description:
------------
This project is a Django backend application designed as part of a city digital twin system.
It provides RESTful API endpoints to manage and retrieve data related to buildings
and cities, as well as an admin panel for data management. The API is built using 
Django REST Framework and connects to a PostgreSQL database.

Features:
---------
- RESTful API endpoints for Buildings and Cities
- API root that lists available endpoints
- Django Admin panel for management
- Environment variable configuration with python-decouple and python-dotenv
- Database URL configuration through dj-database-url
- Superuser management for administrative tasks

Project Structure:
------------------
cityDigitalTwin/
   ├── cityDigitalTwin/             # Django project folder (settings, urls, wsgi, etc.)
   ├── buildings/                   # Django app with models, views, serializers, urls for Buildings and Cities
   ├── templates/                   # HTML templates (includes index.html for homepage)
   ├── manage.py                    # Django command-line utility
   ├── requirements.txt             # Application dependencies
   └── README.txt                   # This file

Installation:
-------------
1. Clone the repository:
   git clone https://github.com/Mahshid98Alm/CityDigitalTwin.git

2. Navigate to the project directory:
   cd CityDigitalTwin

3. (Optional but recommended) Create a virtual environment:
   python3 -m venv myenv

4. Activate the virtual environment:
   source myenv/bin/activate

5. Install the required dependencies:
   pip install -r requirements.txt

6. Configure environment variables:
   - Create a .env file in the project root.
   - Define necessary variables (e.g., SECRET_KEY, DATABASE_URL, DEBUG settings, etc.)
    

7. Run database migrations:
   python manage.py makemigrations
   python manage.py migrate

8. Create a superuser:
   python manage.py createsuperuser

9. Run the development server:
   python manage.py runserver

API Endpoints:
--------------
Once the server is running, you can access the following endpoints:
- API Root:      http://127.0.0.1:8000/api/
- Buildings API: http://127.0.0.1:8000/api/buildings/
- Building Detail: http://127.0.0.1:8000/api/buildings/<uuid:pk>/
- Cities API:    http://127.0.0.1:8000/api/cities/
- City Detail:   http://127.0.0.1:8000/api/cities/<uuid:pk>/
- Admin Panel:   http://127.0.0.1:8000/admin/

Requirements:
-------------
- Python 3.x
- Django 5.x (as specified in requirements.txt)
- Django REST Framework
- dj-database-url
- python-decouple
- python-dotenv
- psycopg2-binary (or psycopg)

Usage:
------
After installation, use the provided API endpoints to integrate with your front-end.
The Django admin panel (http://127.0.0.1:8000/admin/) is available to manage data.
Front-end developers can use these endpoints for further development.

Contributing:
-------------
Feel free to fork and contribute to this project. Please follow standard GitHub
workflow practices (branching, pull requests, etc.) when submitting changes.

License:
--------
This project is open-source and available under the MIT License.


Notes:
------
- Make sure your virtual environment is activated when running commands.
- If you deploy this project, adjust your settings accordingly and disable DEBUG mode.
- For API documentation, consider using Swagger or DRF Spectacular.

-----------------------------------------------------
For any issues or questions, please open an issue on the GitHub repository.
