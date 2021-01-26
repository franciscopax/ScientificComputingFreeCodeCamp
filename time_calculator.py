def add_time(start, dur, day="0"):

    # ------------------
    # Process start time
    time = start.split()
    hours, minutes = time[0].split(':')
    hours, minutes = int(hours), int(minutes)
    amPm = time[1]

    # ------------------
    # Process duration
    duration = dur.split(':')
    durationHours, durationMinutes = duration[0], duration[1]
    durationHours, durationMinutes = int(durationHours), int(durationMinutes)

    # ------------------
    # Process the minutes and adjust the hours if the minutes add up to more than one hour

    finalMinutes = minutes + durationMinutes
    finalHours = 0

    if finalMinutes >= 60:
        finalMinutes = finalMinutes % 10
        durationHours += 1

    # ------------------
    # How many 12 hour cycles are in durationHours

    if durationHours / 12 > 1:
        cycles = int(durationHours / 12)

    # ------------------
    # Hours left in current time to hit the next cycle

    hoursToNextCycle = 12 - hours
    fullDayElapsed = 0

    if durationHours < hoursToNextCycle:
        finalHours = hours + durationHours

    else:
        
        finalHours = hours + durationHours

        for cycle in range(0,finalHours,12):

            if finalHours < 12: 
                break

            if amPm == 'PM': 
                amPm = 'AM'
                fullDayElapsed += 1
            elif amPm == 'AM': 
                amPm = 'PM'

            finalHours -= 12
            if finalHours == 0:
                finalHours = 12
        

    if finalMinutes < 10: finalMinutes = '0' + str(finalMinutes)

    result = f'{finalHours}:{finalMinutes} {amPm}'

    # ------------------
    # Days of the week

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    if day.lower() in days:

        indexOfCurrentDay = days.index(day.lower())
        indexOfFinalDay = indexOfCurrentDay + fullDayElapsed

        finalIndex = indexOfCurrentDay

        for n in range(indexOfCurrentDay,indexOfFinalDay):

            if finalIndex == len(days) - 1:
                finalIndex = 0
            else:
                finalIndex += 1

        result += f', {days[finalIndex].capitalize()}'


    if fullDayElapsed > 0:

        if fullDayElapsed == 1:
            result += ' (next day)'
        else:
            result += f' ({fullDayElapsed} days later)'

    return result
    
    




print(add_time("8:16 PM", "1738:54", "tuesday"))