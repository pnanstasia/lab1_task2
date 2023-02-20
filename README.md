# Lab №1 task №2 (creating a map)
The module is designed to create a map showing the 10 nearest locations where a movie was shot in a given year. 
This module has 6 functions:
- read_file (Function for reading from a file. The function takes two arguments: path to file and year. Returns list of lists with movies and location, where movies were shot of the desired year)
- distance_between_coord (Additional function for finding the distance between coordinates. Function takes 4 arguments: 2 arguments of latitude, 2 arguments of longitude, and returns distance between this points)
- get_coordinates (Additional function takes 1 argument - location, for ex. 'Los Angeles, USA' and returns coordinates of this location)
- fitable_location (Function takes 3 arguments: films (list of films, which you can get from read_file), my_lat and my_lon - coordinates, which you enter to find way. fitable_location returns 10 the closest location to ones you entered)
- the_biggest_num_of_films (Additional function takes 1 argument - list of lists from fitable_location. Every list has 3 elements (1 - coordinates of location, 2 - distance from distance_between_coord, 3 - number of films, which were shot in this location). Function returns 1 list, which has the biggest number of movies, which were shot)
- create_map (Function for creating map, has 4 arguments: 1 - year, 2 - latitude, 3 - longitude, 4 - path to file. The result of the function is the creation of a file with a map, which must be opened in a browser in order to see the result)
Example of input:
![Знімок екрана 2023-02-20 о 18 49 04](https://user-images.githubusercontent.com/116551880/220163987-6557182f-8d33-417c-b149-265b08ae2b30.png)
