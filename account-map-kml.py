import simplekml
from geopy.geocoders import Nominatim
import folium


# Function to read company data from a text file
def read_company_data(file_path):
    company_data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) == 3:
                company_data.append((parts[0], f"{parts[1]}, {parts[2]}"))
    return company_data

# Read company data from the text file
company_data = read_company_data('company_data.txt')


# Initialize the geolocator
geolocator = Nominatim(user_agent="company_locator")

# Create a KML object
kml = simplekml.Kml()

# Create a folium map centered in the USA
map_center = [39.8283, -98.5795]  # Center of the USA
company_map = folium.Map(location=map_center, zoom_start=4)

# Add points to the KML object and folium map for each company
for company, location in company_data:
    try:
        geocode_result = geolocator.geocode(location)
        if geocode_result:
            # Add to KML
            point = kml.newpoint(name=company, description=location)
            point.coords = [(geocode_result.longitude, geocode_result.latitude)]
            
            # Add to folium map
            folium.Marker(
                location=[geocode_result.latitude, geocode_result.longitude],
                popup=f"{company}\n{location}",
                tooltip=company
            ).add_to(company_map)
        else:
            print(f"Geocoding failed for {location}")
    except Exception as e:
        print(f"Error geocoding {location}: {e}")

# Save the KML object to a file
kml.save("companies.kml")

# Save the folium map to an HTML file
company_map.save("companies_map.html")

print("KML file and HTML map created successfully.")