def most_prolific(albums):
    """
    Takes a dictionary with values formatted {'title': year} and returns
    the year that occurs most often among the elements. IF there are years
    that occur the same number of times, it returns a list of years.
    years: dictionary. Holds the years albums were published and the number of
    albums published in that year
    most_prolific_years: list. Holds the years that tied for most albums
    most_albums: integer. Holds the highest number of albums produced in a
    single year.
    """
    years = {} #dictionary that will hold our years and their number of occurences
    most_prolific_years = [] #list to hold years that had the most albums
    most_albums = 0 #value to hold the most albums produced in any one year

    #for each element in our submitted dictionary, add its year to years with a
    #count of one. If the year is already in years, add 1 to the count instead
    for album in albums:
        year = albums[album]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

    #iterate through years to find highest count and set most_albums to that
    #count
    for year in years:
        if years[year] > most_albums:
            most_albums = years[year]

    #add all years that qualify as most_albums to most_prolific_years
    for year in years:
        if years[year] == most_albums:
            most_prolific_years.append(year)

    if len(most_prolific_years) == 1:
        return most_prolific_years[0]
    else:
        return most_prolific_years
