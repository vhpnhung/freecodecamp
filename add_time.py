import math

def calculate_weekday(weekday, add_weekday=0):
    # create 2 dicts
    weekdays_dict = {
        "sunday": 1,
        "monday": 2,
        "tuesday": 3,
        "wednesday": 4,
        "thursday": 5,
        "friday": 6,
        "saturday": 7, 
    }

    reversed_dict = {}
    for key, value in weekdays_dict.items():
        reversed_dict[value] = key.capitalize()
    
    
    # calculate
    if weekdays_dict[weekday.lower()] + add_weekday > 7:
        added_weekday = weekdays_dict[weekday.lower()] + add_weekday - 7
    else:
        added_weekday = weekdays_dict[weekday.lower()] + add_weekday
    added_weekday = reversed_dict[added_weekday]
    return added_weekday


def add_time(time, addition="0", weekday="Monday"):
    more_day=0
    # convert time into 24h
    time_period = time.split(" ")
    time_24 = time_period[0].split(":")
    time_24[0] = int(time_24[0]) if time_period[1].upper() == "AM" else (int(time_24[0])+12)
    time_24[1] = int(time_24[1])

    # convert addtion to int
    addition = addition.split(":")
    addition[0] = int(addition[0])
    addition[1] = int(addition[1])

    # minutes
    if time_24[1]+addition[1] >= 60:
        time_24[1] = time_24[1]+addition[1]-60
        time_24[0] += 1
    else:
        time_24[1] = time_24[1]+addition[1]
    
    # hours
    if time_24[0]+addition[0] >= 24:
        time_24[0] = (time_24[0]+addition[0])%24
        if (time_24[0]+addition[0])/24 <= 1:
            more_day = 1
        else:
            more_day = math.floor((time_24[0]+addition[0])/24)
    else:
        time_24[0] = time_24[0]+addition[0]
    
    # convert time into 12h
    time_12 = ["hour", time_24[1], "AM/PM"]
    if 12<time_24[0]<24:
        time_12[0] = time_24[0]-12     # PM
        time_12[2] = "PM"
    elif time_24[0] == 12:
        time_12[0] = time_24[0]        # PM
        time_12[2] = "PM"
    elif time_24[0] == 24:
        time_12[0] = time_24[0]-24     # AM
        time_12[2] = "AM"
    else:
        time_12[0] = time_24[0]        # AM
        time_12[2] = "AM"
    
    # format to hh:mm AM/PM
    for i in range(2):
        if len(str(time_12[i])) == 1:
            time_12[i] = "0"+str(time_12[i])
        else:
            time_12[i] = str(time_12[i])
    print(f"Result: {time_12[0]}:{time_12[1]} {time_12[2]} ({calculate_weekday(weekday, add_weekday=more_day)})")

add_time("3:00 PM", "3:10")