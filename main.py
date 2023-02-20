def get_coordinates(location_of_city):
    """
    Function returns coordinates of place, where movies were shot
    >>> get_coordinates('Los Angeles, USA')
    (34.0536909, -118.242766)
    >>> get_coordinates('Lviv, Ukraine')
    (49.841952, 24.0315921)
    """
    geolocator = Nominatim(user_agent="https://www.openstreetmap.org/copyright")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    try:
        location = geolocator.geocode(location_of_city)
        if not location:
            return None
    except (AttributeError, GeocoderUnavailable):
        return None
    return location.latitude, location.longitude
