def add_time(start="3:00 PM", duration="2:32", day=False):

    #processing converting from 12 to 24
    if "pm" in start.lower():
        start = start.split(":")
        start[0] = str(int(start[0])+12)
        start = ":".join(start)
        start = start.strip(" PM")
    else:
        start= start.strip(" AM")
    
    start=start.split(":")
    start= list(map(lambda x: int(x), start))
    start=start[0]*60+start[1]

    duration = duration.split(":")
    duration= list(map(lambda x: int(x), duration))
    duration=duration[0]*60+duration[1]
    
    final = ""              #final string to be returned

    time_final =start+duration

    final = "0"*(2-len(str(time_final%60)))+str(time_final%60)      #add minutes to the final string
    time_final = time_final//60

    #converting from 24 to 12
    hours, IS_PM = time_final%24, False
    if hours<13:
        hours = hours
        if hours == 00:
            hours = 12
    else:
        hours, IS_PM = hours%12, True

    final = str(hours)+":"+final    #add hours to final string
    final = final+" "+"PM" if IS_PM else final+" "+"AM"


    #Adding the newday, if passed in argument
    if day:
        week = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
        day = week.index(day.lower())

    time_final = time_final//24     #calculating number of days passed
    if day:
        index = (day+time_final)%7
        final = final+", "+week[index].title()


    #Adding number of days passed, if there
    if time_final:
        if not(time_final==1):
            final = final+" ("+str(time_final)+" days later)"
        else:
            final = final+" (next day)"


    return final
