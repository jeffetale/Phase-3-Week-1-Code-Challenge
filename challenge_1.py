"""
Challenge 1: Converting 12-hour time to 24-hour time
Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, right? Well, let's see if you can do it!

You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input.

Your task is to return a four-digit string that encodes that time in 24-hour time.
"""


def to_24_hour():
    hour = int(input("Enter the hour (1-12): "))
    minute = int(input("Enter the minute (0-59): "))
    period = input("Enter the period (am/pm): ").lower()
    if not isinstance(hour, int):
        return "Error: hour must be an integer"
    if not isinstance(minute, int):
        return "Error: minute must be an integer"
    if not isinstance(period, str):
        return "Error: period must be a string"
    if not (1 <= hour <= 12):
        return "Error: hour must be between 1 and 12"
    if not (0 <= minute <= 59):
        return "Error: minute must be between 0 and 59"
    if period not in ["am", "pm"]:
        return "Error: period must be either 'am' or 'pm'"
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    return f"{hour:02d}{minute:02d}"

result = to_24_hour()
print(f"The 24-hour time is: {result}")