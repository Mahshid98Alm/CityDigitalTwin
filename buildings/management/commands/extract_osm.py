import requests # type: ignore
from django.core.management.base import BaseCommand
from buildings.models import Building # type: ignore

class Command(BaseCommand):
    help = 'Extracts OSM building data for specified cities'

    def add_arguments(self, parser):
        parser.add_argument(
            '--cities',
            nargs='+',  # Allow one or more city names
            type=str,
            help='List of cities to extract OSM data for (e.g., --cities Lisbon Braga)',
        )

    def handle(self, *args, **options):
        # Define the default cities: Braga and Lisbon are both in Portugal.
        default_cities = ['Braga', 'Lisbon']
        cities = options['cities'] if options['cities'] else default_cities

        # Define bounding boxes for each city, formatted as "south,west,north,east"
        city_bounds = {
            'Braga': '41.45,-8.5,41.65,-8.3',   # Approximate bounding box for Braga
            'Lisbon': '38.65,-9.20,38.80,-9.00',  # Approximate bounding box for Lisbon
        }

        for city in cities:
            bounds = city_bounds.get(city)
            if not bounds:
                self.stdout.write(self.style.WARNING(f"No geographic bounds defined for {city}. Skipping."))
                continue

            # Build an Overpass API query using the bounding box
            query = f"""
            [out:json];
            (
              way["building"]({bounds});
            );
            out body;
            >;
            out skel qt;
            """
            self.stdout.write(self.style.NOTICE(f"Processing {city} with bounds {bounds}..."))

            response = requests.get('http://overpass-api.de/api/interpreter', params={'data': query})
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f"Error retrieving data for {city}"))
                continue

            data = response.json()

            # Process OSM building elements
            for element in data.get('elements', []):
                if element.get('type') == 'way' and 'tags' in element:
                    osm_tags = element['tags']
                    building = Building(
                        name=osm_tags.get('name', ''),
                        address=osm_tags.get('addr:full', ''),
                        city=city,  # Set the city
                        osm_data=element,
                        geometry={"nodes": element.get("nodes", [])}
                    )
                    building.save()
                    self.stdout.write(self.style.SUCCESS(f"Saved building: {building.name or 'Unnamed'} in {city}"))

            self.stdout.write(self.style.SUCCESS(f"Finished processing for {city}."))
