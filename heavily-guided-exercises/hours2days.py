def hours2days(hours):
    """
    Function that takes input hours and returns how many days that is,
    and how many leftover hours. E.g., 26 hours = 1 day and 2 hours.
    """

    days = hours//24
    hours_remaining = hours%24

    return (days, hours_remaining)

print(hours2days(24)) # 24 hours is one day and zero hours
print(hours2days(25)) # 25 hours is one day and one hour
print(hours2days(10000)) # 10000 hours is 416 days and 16 hours
