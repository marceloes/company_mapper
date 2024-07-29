### README.md

# Company Location Mapper

This project reads company data from a text file, geocodes the locations, and generates both a KML file and an HTML interactive map with pins for each company's location.

## Functionality

- **Read Company Data**: Reads company names and locations from a text file.
- **Geocode Locations**: Uses the Nominatim geocoding service to convert addresses into latitude and longitude coordinates.
- **Generate KML File**: Creates a KML file with placemarks for each company.
- **Generate HTML Map**: Creates an interactive HTML map with markers for each company.

## Prerequisites

- Python 3.x
- `geopy` library
- `folium` library
- `simplekml` library

You can install the required libraries using pip:

```sh
pip install geopy folium simplekml
```

## How to Run the Code

1. **Prepare the Text File**: Create a text file named `company_data.txt` with the following format:
    ```
    Company Name, City, State
    ```

    Example:
    ```
    ACME Corp, Springfield, IL
    Globex Corporation, Metropolis, NY
    Initech, Palo Alto, CA
    ```

2. **Run the Script**: Execute the Python script to generate the KML file and HTML map.

    ```sh
    python account-map-kml.py
    ```

3. **Output**: The script will generate two files:
    - `companies.kml`: A KML file with placemarks for each company.
    - `companies_map.html`: An interactive HTML map with markers for each company.

## Example `company_data.txt`

```
ACME Corp, Springfield, IL
Globex Corporation, Metropolis, NY
Initech, Palo Alto, CA
Umbrella Corporation, Raccoon City, MI
Wayne Enterprises, Gotham, NJ
Stark Industries, Los Angeles, CA
Wonka Industries, Hershey, PA
Hooli, San Francisco, CA
Soylent Corp, New York, NY
Tyrell Corporation, Los Angeles, CA
```

## Notes

- Ensure that the `company_data.txt` file is in the same directory as the Python script.
- The script uses the Nominatim geocoding service, which may have usage limits. Consider using an API key if you encounter rate limits.

## License

This project is licensed under the MIT License. See the LICENSE file for details.