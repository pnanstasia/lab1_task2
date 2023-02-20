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
