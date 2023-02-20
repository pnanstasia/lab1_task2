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
