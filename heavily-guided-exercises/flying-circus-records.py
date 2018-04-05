def total_takings(monthly_takings):
    """
    Calculates the sum of takings from every circus this year

    monthly_takings: dictionary. Keys with month names, values
    with lists containing the money taken from each event in that
    month, in order that the events happened.
    """
    # TODO: Implement this function

    takings = 0 #the value we'll store the sum of takings in

    #for each month key, add each value from attached list to takings
    for month in monthly_takings:
        events = monthly_takings[month]
        for event in events:
            takings += event

    return takings

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

print(total_takings(monthly_takings))
