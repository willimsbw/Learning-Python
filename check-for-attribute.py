import turtle

def checkSet(object, attribute, searchValue):
    """
    Checks object for an attribute. If it has that attribute but the value,
    in it is different from searchValue, returns the value the attribute is set
    to. If the value and searchValue match, returns a statement letting you know.
    If the object lacks the attribute, adds it with value searchValue.

    object: an object
    attribute: string. The name of the attribute whose value you want to find or set.
    searchValue: the value you think they attribute contains, or you want to set
    the attribute to if it doesn't exist
    """

    #if it gets an AttributeError because the attribute doesn't exist, adds the attribute to the object
    try:
        getattrResult = getattr(object, attribute)
        print(getattrResult)
    except AttributeError:
        print("Object lacks this attribute. Adding, with value " + str(searchValue))
        setattr(object, attribute, searchValue)
        return

    if getattrResult == searchValue:
        print("You were right! the object has attribute " + attribute + " and its value is " + str(searchValue) + ".")
        return
    else:
        print("Object has attribute " + attribute + " but its value isn't " + str(searchValue) + ". It was " + str(getattrResult))

brad = turtle.Turtle()
checkSet(brad, "color", "black")
checkSet(brad, "gummy bears", True)
checkSet(brad, "gummy bears", False)
