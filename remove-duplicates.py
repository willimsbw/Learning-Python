# Define the remove_duplicates function
def remove_duplicates(list):
    """
    Take a list of values and return a version of that list
    with all duplicate values removed, retaining one of each
    value that is duplicated
    """

    #list that we'll move values into and return
    return_list = []

    #for each value, push it into return_list if it's not already
    #in return_list
    for value in list:
        if value not in return_list:
            return_list.append(value)

    return return_list

print(remove_duplicates(["a", "b", "c", "d", "d", "d", "a", "c"]))
