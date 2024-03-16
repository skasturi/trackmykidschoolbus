import requests

"""
Methods to track the bus location
"""

"""
Logic:

Bus live location is available at the following url. Replace <n> with the route number.
https://trac.suveechi.com/k/m.php?k=CHK-R<n>

This url in turn loads up: 
https://trac.suveechi.com/k/mmap.php?k=CHK-R<n>

As part the content of the mmap.php, following piece of code is found: 
<body onload="initialize_map(); add_map_point(13.0113590, 77.7392334);">
  <div id="map" style="width: 100vw; height: 100vh;"></div>
</body>
</html>

13.0113590 -> Latitude
77.7392334 -> Longitude
"""

bus_route_number = 10


def track_bus_location(bus_route_number):
    # Define the URL
    url = f"https://trac.suveechi.com/k/mmap.php?k=CHK-R{bus_route_number}"
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the contents of the response
        content = response.text
        # Find the last occurrence of "add_map_point("
        start_index = content.rfind("add_map_point(") + len("add_map_point(")
        end_index = content.find(");", start_index)
        coordinates = content[start_index:end_index].split(", ")
        # Extract the latitude and longitude values
        latitude = float(coordinates[0])
        longitude = float(coordinates[1])
        
        # Return the latitude and longitude values
        return latitude, longitude
    else:
        print("Failed to fetch the URL:", response.status_code)

        # Return None if the request was not successful
        return None, None

# Call the function with the bus route number
latitude, longitude = track_bus_location(bus_route_number)
if latitude is not None and longitude is not None:
    print("Latitude:", latitude)
    print("Longitude:", longitude)
else:
    print("Failed to track bus location.")