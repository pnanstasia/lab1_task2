"""
Module for working with map
"""
import argparse
import math
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderUnavailable
parser = argparse.ArgumentParser()
parser.add_argument("year", type=int)
parser.add_argument("my_lat", type=float)
parser.add_argument("my_lon", type=float)
parser.add_argument("path_to_file", type=str)
args = parser.parse_args()

def read_file(path_to_file, year):
    """
    Function for reading file
    """
    result = []
    with open(path_to_file, encoding='utf-8') as file:
        work = file.readlines()
        for lines in work:
            if lines.startswith('"'):
                result.append(lines.strip('\n').split('\t'))
    work_list = []
    for elements in result:
        temp = []
        for value in elements:
            if (value != '') and (not value.startswith('(')):
                temp.append(value)
        work_list.append(temp)
    fitable_films = []
    for i in work_list:
        if str(year) in i[0]:
            fitable_films.append(i)
    return fitable_films

def distance_between_coord(lat_1, lon_1, lat_2, lon_2):
    """
    Function for find the least way between coordinates
    >>> distance_between_coord(49.91234, 24.01235, -13.67543, 3.87234)
    7340047.124871838
    >>> distance_between_coord(-49.09875, -24.01235, -13.67543, -3.87234)
    4348279.467920308
    """
    radius = 6371000
    an_f1 = lat_1 * math.pi / 180
    an_f2 = lat_2 * math.pi / 180
    an_f0 = (lat_2 - lat_1) * math.pi / 180
    an_d0 = (lon_2 - lon_1) * math.pi / 180
    const_a = ((math.sin(an_f0/2)) ** 2) + (math.cos(an_f1) * math.cos(an_f2) *\
                                             ((math.sin(an_d0/2)) ** 2))
    const_c = 2 * math.atan2(math.sqrt(const_a), math.sqrt(1-const_a))
    distance = radius * const_c
    return distance

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

def fitable_location(films, my_lat, my_lon):
    """
    Function returns 10 location which are the closest
    """
    list_of_all_coord = []
    for elem in films:
        coord = get_coordinates(elem[1])
        if not coord:
            continue
        list_of_all_coord.append(coord)
    sort_coords = dict()
    for coord in list_of_all_coord:
        if coord not in sort_coords:
            counter = list_of_all_coord.count(coord)
            sort_coords.update({coord:counter})
    dist = []
    for keys in sort_coords.keys():
        distance = distance_between_coord(my_lat, my_lon, keys[0], keys[1])
        dist.append([keys,(distance)])
    sorted_dist = sorted(dist, key=lambda x: x[1])[:10]
    for j in sorted_dist:
        add = sort_coords[j[0]]
        j.append(add)
    return sorted_dist

def the_biggest_num_of_films(list_of_movies):
    """
    Function returns coordinates, of place, where were shot the biggest number of movies
    >>> the_biggest_num_of_films([[(49.841952, 24.0315921), 4348279.467920308, 9], \
[(34.0536909, -118.242766), 8743198.070462689, 3]])
    [(49.841952, 24.0315921), 4348279.467920308, 9]
    """
    max_number = 1
    for element in list_of_movies:
        if element[2] > max_number:
            max_number = element[2]
            result = element
    return result

def create_map(year, lat, lon, path_to_file):
    """
    Function for creating map
    """
    map = folium.Map(location=[lat, lon],zoom_start=1)
    html = """<h4>Information:</h4>
    Year: {} <br>
    Number of movies: {}
    """
    figure = folium.FeatureGroup(name='10 the closest movies')
    new_figure = folium.FeatureGroup(name='Location, where were shot the biggest number of movies')
    figure_ucu = folium.FeatureGroup(name='Location UCU')
    list_movies = read_file(path_to_file, year)
    fit_loc = fitable_location(list_movies, lat, lon)
    for i in fit_loc:
        iframe = folium.IFrame(html=html.format(year, i[2]),
                        width=300,
                        height=100)
        figure.add_child(folium.Marker(location=[i[0][0], i[0][1]],
                popup=folium.Popup(iframe),
                icon=folium.Icon(color = "beige", icon="fa-clapperboard", prefix="fa")))
        map.add_child(figure)
    the_biggest = the_biggest_num_of_films(fit_loc)
    new_figure.add_child(folium.Marker(location=[the_biggest[0][0], the_biggest[0][1]],
                popup=folium.Popup(iframe),
                icon=folium.Icon(color = "red", icon="fa-film", prefix="fa")))
    map.add_child(new_figure)
    figure_ucu.add_child(folium.Marker(location=[49.817545, 24.023932],
                popup=folium.Popup(iframe),
                titles = ('UCU'),
                icon=folium.Icon(color = "lightred", icon="fa-school", prefix="fa")))
    map.add_child(figure_ucu)
    map.add_child(folium.LayerControl())
    map.save('map_movies.html')

create_map(args.year, args.my_lat, args.my_lon, args.path_to_file)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
