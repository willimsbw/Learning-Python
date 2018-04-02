import re

def create_cast_list(filename):
    """
    Takes a cast list from IMDB and pulls a string up to the first comma
    (actors' names), and puts that string into a list, which gets returned.
    filename: txt file. The file containing the cast list
    """

    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    regex = re.compile("[^,]*") #matches all values up to first comma

    #open the file flying-circus-cast.txt
    with open(filename) as txt:
        #for each line in the file
        for line in txt:
            #use regex to find the characters up to the first comma, then export
            #those characters as a string to cast_list
            cast_list.append(regex.search(line))

    return cast_list

print(create_cast_list("c:/version-control/learning-python/create-cast-list/flying-circus-cast.txt"))
