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
