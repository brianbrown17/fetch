import requests

def nearby_search(api_key, location, radius, keyword=None, type=None):
    """
    Perform a nearby search using the Google Places API.

    Args:
    - api_key (str): Your Google Cloud API key.
    - location (str): Latitude and longitude coordinates (e.g., "40.712776,-74.005974").
    - radius (int): The radius (in meters) around the location to search within.
    - keyword (str, optional): A term to be matched against all available fields, including name, type, and address, of the places. 
    - type (str, optional): Restricts the results to places matching the specified type.

    Returns:
    - dict: JSON response containing details of places matching the query.
    """
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": api_key,
        "location": location,
        "radius": radius,
        "keyword": keyword,
        "type": type
    }
    response = requests.get(endpoint, params=params)
    return response.json()

def text_search(api_key, query, location=None, radius=None):
    """
    Perform a text search using the Google Places API.

    Args:
    - api_key (str): Your Google Cloud API key.
    - query (str): The text query to search for (e.g., "parks in New York").
    - location (str, optional): Latitude and longitude coordinates (e.g., "40.712776,-74.005974").
    - radius (int, optional): The radius (in meters) around the location to search within.

    Returns:
    - dict: JSON response containing details of places matching the query.
    """
    endpoint = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "key": api_key,
        "query": query,
        "location": location,
        "radius": radius
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Example usage:
api_key = "YOUR_API_KEY"
location = "40.712776,-74.005974"  # Example: New York City coordinates
radius = 5000  # Search radius in meters
keyword = "park"
type = "park"  # You can specify the type to narrow down the search

# Perform a nearby search
nearby_results = nearby_search(api_key, location, radius, keyword=keyword, type=type)
print(nearby_results)

# Perform a text search
query = "parks in New York"
text_results = text_search(api_key, query, location=location, radius=radius)
print(text_results)