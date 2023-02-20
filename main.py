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
