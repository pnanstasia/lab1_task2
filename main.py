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
